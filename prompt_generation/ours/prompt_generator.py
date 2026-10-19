import textwrap
from typing import List, Mapping, Optional, Sequence, Union
from .config import TopicControlledConfig


class PromptGenerator:
    def __init__(
        self,
        few_shot_examples: Union[
            Sequence[dict], Mapping[Union[int, str], Sequence[dict]]
        ],
        target_language: str,
    ):
        self.few_shot_examples = few_shot_examples
        self.target_language = target_language

    def get_few_shot_pool(self, config: TopicControlledConfig) -> List[dict]:
        if isinstance(self.few_shot_examples, Mapping):
            bucket = (
                "paragraph"
                if config.few_shot_sentence_length == 25
                else str(config.few_shot_sentence_length)
            )
            return list(self.few_shot_examples.get(bucket, []))
        return list(self.few_shot_examples)

    def build_prompt(
        self,
        config: TopicControlledConfig,
        word_candidates_text: str,
        topic: Optional[str] = None,
        few_shot_examples_override: Optional[Sequence[dict]] = None,
    ) -> str:
        target_language = self.target_language[:1].upper() + self.target_language[1:]
        selected = (
            few_shot_examples_override
            if few_shot_examples_override is not None
            else self.get_few_shot_pool(config)[: config.n_few_shot]
        )

        few_shot_text = "\n\n".join(
            f"Example {i}\n\nWord Candidates:\n{ex['word_candidates']}\n\nOutput:\n{ex['output']}"
            for i, ex in enumerate(selected, 1)
        )

        if config.target_sentence_length == 25:
            output_type, reqs = (
                "paragraph",
                "- Output a paragraph containing at least 3 sentences.\n- The paragraph must contain at least 25 words.",
            )
        else:
            output_type, reqs = (
                "sentence",
                f"- Output exactly one sentence.\n- The sentence should be around {config.target_sentence_length} words.",
            )

        topic_rule = (
            f"\nTOPIC:\n- Keep the output related to '{topic}' where the vocabulary allows.\n"
            if topic else ""
        )

        prompt = textwrap.dedent(f"""
You are a linguistic expert in {target_language}.

TASK: Create one coherent {output_type} in {target_language} that sounds natural and fluent to a native speaker.

===
RULES (MUST FOLLOW):
===
VOCABULARY:
- Each entry in the "Word Candidates" list follows this structure, separated by " | ":
  <word> | <part-of-speech> | <meaning> | <example_usage>
  where:
  - <word>: the {target_language} word to use.
  - <part-of-speech>: the grammatical role of the word (e.g., noun, verb, adjective).
  - <meaning>: the English meaning of the word.
  - <example_usage>: one or more example sentences in {target_language} showing how the word is naturally used for reference only. If multiple examples are given, they are separated by " * ".
- Use the word candidates list as vocabulary guidance rather than a strict requirement.
- Try to use the candidate words where they fit naturally in the output.

{topic_rule}
PUNCTUATION & CASING:
- You ARE allowed to use standard punctuation (periods, commas, question marks).
- You ARE allowed to capitalize the first letter of a word to start the output or for proper nouns.

LENGTH & COVERAGE:
{reqs}

QUALITY:
- The output must be grammatically correct in {target_language}.
- DO NOT prioritize length over logical coherence. Prioritize natural, coherent, and meaningful output.
- DO NOT use specialized/technical terms unless they fit the context perfectly.

ORIGINALITY:
- Do not reuse the main entities, events, or semantic content from any few-shot example.
- Do not create output that is a paraphrase, extension, recombination, or slight modification of a few-shot example.

===
FEW-SHOT EXAMPLES ({len(selected)} Examples)
===
{few_shot_text}
===
END OF EXAMPLES.
===

Generate a new, unique {output_type} based on the candidates below:
===
WORD CANDIDATES:
{word_candidates_text}
===

Return only the {output_type}.
        """).strip()
        return prompt
