"""Configuration for few-shot-only generation."""

from dataclasses import dataclass


@dataclass
class FewShotExperimentConfig:
    target_sentence_length: str  # "5", "10", "15", "20", or "paragraph"
    n_few_shot: int  # number of few-shot examples per prompt
    few_shot_sentence_length: str = "5"  # which few-shot bucket to draw from
