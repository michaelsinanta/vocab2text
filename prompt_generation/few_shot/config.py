"""
Hyperparameter Configuration (few-shot only)
"""

from dataclasses import dataclass

from prompt_generation.config import LENGTH_CLI


@dataclass
class ExperimentConfig:
    """Configuration for a single few-shot prompt run"""

    exp_id: str
    target_sentence_length: str  # "5", "10", "15", "20", or "paragraph"
    n_few_shot: int  # number of few-shot examples per prompt
    few_shot_sentence_length: str = "5"  # which few-shot bucket to draw from

    def __str__(self):
        return (
            f"Exp_{self.exp_id}: "
            f"length={self.target_sentence_length}, "
            f"few_shot={self.n_few_shot}, "
            f"few_shot_len={self.few_shot_sentence_length}"
        )


FEW_SHOT_LENGTH_OPTIONS = tuple(LENGTH_CLI.values())
