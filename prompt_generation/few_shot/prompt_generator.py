"""
Few-shot-only prompt generator.

Builds a prompt that contains only few-shot example outputs
"""

import random
from typing import Dict, List, Mapping, Optional, Sequence, Tuple

from few_shot_prompts.registry import FewShotInput, get_pool, normalize_length
from few_shot_prompts.types import FewShotExample
from prompt_generation.config import (
    PARAGRAPH_BUCKET,
    bucket_filename,
    language_display_name,
)
from prompt_generation.few_shot.config import ExperimentConfig

PROMPT_TEMPLATE = """\
You are a linguistic expert in {language}.

TASK: Create one coherent {output_type} in {language}.

===
RULES (MUST FOLLOW):
===
1. FEW-SHOT GUIDANCE:
- Use the few-shot examples only as guidance for writing style, grammar, fluency, and natural sentence structure.
- Do not reuse the main entities, events, or semantic content from any few-shot example.
- Do not create output that is a paraphrase, extension, recombination, or slight modification of a few-shot example.

2. PUNCTUATION & CASING:
- You ARE allowed to use standard punctuation.
- You ARE allowed to capitalize the first letter of a word.

3. LENGTH & COVERAGE:
{length_instruction}

4. QUALITY:
- The output must be grammatically correct in {language}.
- Prioritize natural, coherent, and meaningful output.

===
FEW-SHOT EXAMPLES ({n_examples} Examples)
===
{few_shot_text}
===
END OF EXAMPLES.
===

Return only the {output_type}."""


class FewShotPromptGenerator:
    """Generates few-shot-only prompts."""

    def __init__(
        self,
        few_shot_examples: FewShotInput,
        target_language: str = "Minangkabau",
    ):
        """
        Args:
            few_shot_examples: either a flat list of examples, or a mapping
                from length bucket -> examples
                (e.g. {"5": [...], "paragraph": [...]}).
            target_language: target language name.
        """
        self.few_shot_examples = few_shot_examples
        self.target_language = target_language
        self._uses_length_buckets = isinstance(few_shot_examples, Mapping)

    # ------------------------------------------------------------ helpers
    def _pool_for_config(self, config: ExperimentConfig) -> List[Dict[str, str]]:
        if isinstance(self.few_shot_examples, str):
            raise TypeError(
                "Pre-rendered few-shot strings cannot be filtered by length."
            )

        if self._uses_length_buckets:
            return list(
                get_pool(self.few_shot_examples, config.few_shot_sentence_length)
            )
        return list(self.few_shot_examples)

    @staticmethod
    def format_outputs(examples: Sequence[FewShotExample]) -> str:
        return "\n".join(
            f"Example {i}: {ex['output']}" for i, ex in enumerate(examples, 1)
        )

    @staticmethod
    def _length_spec(config: ExperimentConfig) -> Tuple[str, str]:
        """Return (output_type, length_instruction) for the target length."""
        bucket = normalize_length(config.target_sentence_length)
        if bucket == PARAGRAPH_BUCKET:
            return "paragraph", (
                "- Output a paragraph containing at least 3 sentences.\n"
                "- The paragraph must contain at least 25 words."
            )
        return "sentence", (
            "- Output exactly one sentence.\n"
            f"- The sentence should be around {bucket} words."
        )

    def select_examples(
        self,
        config: ExperimentConfig,
        seed: Optional[int] = None,
        override: Optional[Sequence[FewShotExample]] = None,
    ) -> List[FewShotExample]:
        requested = int(config.n_few_shot)
        pool = self._pool_for_config(config)

        if requested <= 0 or not pool:
            if requested > 0 and self._uses_length_buckets:
                bucket = normalize_length(config.few_shot_sentence_length)
                raise ValueError(
                    f"No few-shot examples for length '{bucket}'. "
                    f"Add EXAMPLES to few_shot_prompts/<language>/"
                    f"{bucket_filename(bucket)}."
                )
            return []

        n = min(requested, len(pool))
        if override is not None:
            return list(override)[:n]

        return random.Random(seed).sample(pool, n)  # shuffled per seed

    # ------------------------------------------------------------ main API
    def generate_prompt_few_shots_only(
        self,
        config: ExperimentConfig,
        seed: Optional[int] = None,
        few_shot_examples_override: Optional[Sequence[FewShotExample]] = None,
    ) -> Tuple[str, str]:
        """Return (prompt, few_shot_text)."""
        language = language_display_name(self.target_language)
        examples = self.select_examples(config, seed, few_shot_examples_override)
        few_shot_text = self.format_outputs(examples)
        output_type, length_instruction = self._length_spec(config)

        prompt = PROMPT_TEMPLATE.format(
            language=language,
            output_type=output_type,
            length_instruction=length_instruction,
            n_examples=len(examples),
            few_shot_text=few_shot_text,
        )
        return prompt, few_shot_text
