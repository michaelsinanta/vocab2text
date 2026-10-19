"""Generate topic-controlled prompts for a single configuration.

This is where candidate_selector.py (word sampling) and prompt_generator.py
(text templating) get wired together. Per prompt, the flow is:

  1. Pick a handful of few-shot demonstration examples for this length bucket.
  2. Pick a topic.
  3. Sample the REAL word-candidate list purely via the configured method
     (CandidateSelector.select(), see candidate_selector.py).
  4. For each selected few-shot example, rebuild its "Word Candidates" text
     by filler words drawn from completely random samples of the dictionary.
  5. Hand everything to PromptGenerator.build_prompt() to get the final string.
"""

import random
import uuid
from typing import Dict, List, Mapping, Optional, Sequence, Union
import pandas as pd
from .config import TopicControlledConfig
from .candidate_selector import CandidateSelector
from .prompt_generator import PromptGenerator
from prompt_generation.config import TOPICS


def _parse_lines(word_candidates: str) -> Dict[str, str]:
    """
    Turn a "word | pos | meaning | example" text block into
    {word: "word | pos | meaning | example"} so we can look up a
    specific word's full line later (used when rebuilding few-shot demo
    text in step 4 above).
    """
    return {
        line.split("|", 1)[0].strip(): line.strip()
        for line in word_candidates.splitlines()
        if line.strip() and line.split("|", 1)[0].strip()
    }


class PromptRunner:
    def __init__(
        self,
        lang_df: pd.DataFrame,
        few_shot_examples: Union[
            Sequence[dict], Mapping[Union[int, str], Sequence[dict]]
        ],
        target_language: str,
    ):
        """
        lang_df: target-language dictionary, already enriched with
                 freq/rank/probs/topic columns (see
                 frequency_similarity.prepare_language_dictionary).
        few_shot_examples: hand-written demonstration examples, either a
                 flat list or keyed by sentence-length bucket (see
                 PromptGenerator's docstring).
        """
        self.target_language = target_language
        self.selector = CandidateSelector(lang_df)
        self.prompt_generator = PromptGenerator(few_shot_examples, target_language)

    def generate_prompts(
        self,
        config: TopicControlledConfig,
        n_samples: int = 5,
        seed: Optional[int] = None,
        topics: Optional[Sequence[str]] = None,
    ) -> List[dict]:
        """
        Generate `n_samples` independent prompts for a single config.
        """
        prompts = []
        for i in range(n_samples):
            rnd = random.Random(None if seed is None else seed + i)

            # 1. Pick which few-shot demo templates to show
            pool = list(self.prompt_generator.get_few_shot_pool(config))
            rnd.shuffle(pool)
            selected_templates = pool[: min(config.n_few_shot, len(pool))]

            # 2. Pick a topic
            topic = config.topic or (
                topics[i % len(topics)] if topics else rnd.choice(TOPICS)
            )

            # 3. Sample the word-candidate list
            candidate_seed = None if seed is None else rnd.randint(0, 2**31 - 1)
            candidates = self.selector.select(config, topic, seed=candidate_seed)

            # 4. Rebuild few-shot example's "Word Candidates"
            override_examples = []
            full_dict = self.selector.df
            word_col = "word" if "word" in full_dict.columns else "direct_translation"

            for tpl in selected_templates:
                ex_rnd = random.Random(rnd.random())

                # The words this template's OWN output actually needs --
                # resolved straight from the template text itself.
                tpl_lines = _parse_lines(tpl["word_candidates"])
                tpl_words = list(tpl_lines.keys())

                # Pool to draw filler words from: the whole dictionary,
                # minus whatever words this template already uses (so a
                # word never appears twice in the same demo block).
                filler_pool = full_dict[~full_dict[word_col].isin(tpl_words)]
                n_filler = max(0, config.n_candidates - len(tpl_words))
                filler_rows = filler_pool.sample(
                    n=min(n_filler, len(filler_pool)),
                    random_state=ex_rnd.randint(0, 2**31 - 1),
                ).to_dict("records")

                ex_rnd.shuffle(tpl_words)
                ex_rnd.shuffle(filler_rows)

                # Combine: all of the template's real words + the freshly
                # sampled filler rows, interleaved randomly.
                combined = [("tpl", w) for w in tpl_words] + [
                    ("filler", r) for r in filler_rows
                ]
                ex_rnd.shuffle(combined)

                lines = []
                for kind, item in combined:
                    if kind == "tpl":
                        # Use the template's own original line verbatim.
                        lines.append(tpl_lines[item])  # type: ignore
                    else:
                        # Build a "word | pos | meaning | example" line from
                        # the freshly sampled (unrelated) filler row.
                        w = item.get(word_col, item.get("word", "N/A"))  # type: ignore
                        pos = item.get("pos_mapped", "N/A")  # type: ignore
                        m = item.get("meaning_translated", w)  # type: ignore
                        ex = item.get("example", "N/A")  # type: ignore
                        lines.append(f"{w} | {pos} | {m} | {ex}")

                override_examples.append(
                    {"word_candidates": "\n".join(lines), "output": tpl["output"]}
                )

            # 5. Assemble the final prompt text
            prompt = self.prompt_generator.build_prompt(
                config,
                self.selector.format_candidates_for_prompt(candidates),
                topic,
                override_examples,
            )

            prompts.append(
                {
                    "prompt_id": str(uuid.uuid4()),
                    "language": self.target_language,
                    "topic": topic,
                    "prompt": prompt,
                    "seed": seed,
                    "candidate_seed": candidate_seed,
                    "n_candidates_actual": len(candidates),
                    "n_few_shot_used": len(selected_templates),
                }
            )
        return prompts
