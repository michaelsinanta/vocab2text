"""Configuration for topic-controlled candidate and prompt generation."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TopicControlledConfig:
    n_candidates: int  # how many words candidates to offer as its vocabulary
    rank_border: int  # frequency-rank cutoff: words at or below this rank count as "high-frequency"
    composition: float  # fraction (0-1) of n_candidates that should come from the high-frequency pool
    top_p_similarity: float  # keep only the top this-fraction of low-frequency words by topic similarity
    target_sentence_length: int = 5
    n_few_shot: int = 3  # how many few-shot examples to include in the prompt
    few_shot_sentence_length: int = 5  # which length of few-shot examples to draw from
    topic: Optional[str] = None
