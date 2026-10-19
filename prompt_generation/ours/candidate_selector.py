"""
This is the core topic-controlled sampling logic: choose frequency-weighted candidates
while biasing the low-frequency portion toward a selected topic.

All sampling entry points accept an optional `seed`. Passing the same seed
(and the same input data) reproduces the exact same candidate set; leaving
it as None falls back to non-deterministic sampling, same as before.
"""

import numpy as np
import pandas as pd
from typing import Optional, Union
from .config import TopicControlledConfig

RngLike = Optional[Union[int, np.random.Generator]]


def _as_rng(seed: RngLike) -> np.random.Generator:
    """
    Normalize a seed (int / None / already-a-Generator) into a
    np.random.Generator. Centralizing this means every sampling call in
    this module draws from the same rng instance when a seed is threaded
    through, instead of silently falling back to the shared global numpy
    random state.
    """
    if isinstance(seed, np.random.Generator):
        return seed
    return np.random.default_rng(seed)


def _weighted_sample_without_replacement(
    pool: pd.DataFrame, n: int, weight_col: str, rng: np.random.Generator
) -> pd.DataFrame:
    """
    Draw `n` rows from `pool` without replacement, with probability
    proportional to `pool[weight_col]`. Used anywhere sampling needs to
    respect frequency ("probs" column) rather than being purely uniform.
    """
    n = min(n, len(pool))
    if n <= 0:
        return pool.iloc[0:0]
    weights = pool[weight_col].to_numpy(dtype=np.float64)
    weights = weights / weights.sum()
    idx = rng.choice(len(pool), size=n, replace=False, p=weights)
    return pool.iloc[idx]


class CandidateSelector:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy().reset_index(drop=True)

    def select_topic_controlled(
        self,
        config: TopicControlledConfig,
        topic: Optional[str] = None,
        pool_df: Optional[pd.DataFrame] = None,
        seed: RngLike = None,
    ) -> pd.DataFrame:
        rng = _as_rng(seed)
        df = pool_df if pool_df is not None else self.df
        chosen_topic = topic or config.topic

        if not chosen_topic:
            raise ValueError("A topic must be specified for topic-controlled sampling.")

        valid_df = df.dropna(subset=["freq", "rank", "probs"])

        # Calculates how many total words should come from the high-frequency pool, based on your composition ratio (e.g., 20% of 100 candidates = 20 words).
        n_high = round(config.n_candidates * config.composition)

        # Calculates the remaining number of words that must be filled by the low-frequency/topic-related pool.
        n_low = config.n_candidates - n_high

        # Isolates common words whose frequency rank is less than or equal to the rank_border (e.g., top 100 words) and have a probability greater than zero.
        pool_high = valid_df[
            (valid_df["rank"] <= config.rank_border) & (valid_df["probs"] > 0)
        ]
        high_sample = _weighted_sample_without_replacement(
            pool_high, n_high, "probs", rng
        )

        # Low-frequency/topic pool: rarer words, filtered by topic relevance
        pool_low = valid_df[valid_df["rank"] > config.rank_border].dropna(
            subset=[chosen_topic]
        )

        # Keep only the top X% most topic-similar words
        cutoff_n = max(1, int(len(pool_low) * config.top_p_similarity))
        pool_low = pool_low.nlargest(cutoff_n, chosen_topic)
        pool_low = pool_low[pool_low["probs"] > 0]
        low_sample = _weighted_sample_without_replacement(pool_low, n_low, "probs", rng)

        result = pd.concat([high_sample, low_sample])

        # Top up with any remaining valid words if either pool came up short
        # (e.g. not enough topic-relevant rare words existed).
        if len(result) < config.n_candidates:
            needed = config.n_candidates - len(result)
            leftover = valid_df.loc[~valid_df.index.isin(result.index)]
            leftover = leftover[leftover["probs"] > 0]
            if len(leftover) > 0:
                result = pd.concat(
                    [
                        result,
                        _weighted_sample_without_replacement(
                            leftover, needed, "probs", rng
                        ),
                    ]
                )

        result["sampled_topic"] = chosen_topic
        return result.sample(frac=1, random_state=rng).reset_index(drop=True)

    def select(
        self,
        config: TopicControlledConfig,
        topic: Optional[str] = None,
        pool_df: Optional[pd.DataFrame] = None,
        seed: RngLike = None,
    ) -> pd.DataFrame:
        return self.select_topic_controlled(
            config,
            topic=topic,
            pool_df=pool_df if pool_df is not None else self.df,
            seed=seed,
        )

    @staticmethod
    def format_candidates_for_prompt(candidates: pd.DataFrame) -> str:
        lines = []
        for _, row in candidates.iterrows():
            w = row.get("word", "N/A")
            pos = row.get("pos_mapped", "N/A")
            m = row.get("meaning_translated", "N/A")
            ex = row.get("example", "N/A")
            pos = "N/A" if pd.isna(pos) or not str(pos).strip() else pos
            m = "N/A" if pd.isna(m) or not str(m).strip() else m
            ex = "N/A" if pd.isna(ex) or not str(ex).strip() else ex
            lines.append(f"{w} | {pos} | {m} | {ex}")
        return "\n".join(lines)
