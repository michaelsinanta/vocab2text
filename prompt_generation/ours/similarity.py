"""
English Word-Topic Similarity

Loads precomputed semantic similarity between every English word and each of the 20
topics from a CSV, then reuses that single table across all target languages by
joining on `anchor_word` — the specific English word each target-language
entry maps to via its `direct_translation`.
"""

import numpy as np
import pandas as pd

from prompt_generation.config import TOPICS


# =====================================================================
# 1. Load English word x topic similarity from CSV
# =====================================================================
def load_english_similarity(
    csv_path: str = "english_word_freq/english_word_topic_similarity.csv",
) -> pd.DataFrame:
    """
    Loads the precomputed English word-topic similarity DataFrame.
    Expected columns: word, <topic_1...20>, freq, rank.
    """
    print(f"Loading precomputed similarity table from {csv_path}")
    return pd.read_csv(csv_path)


def build_similarity_lookup(english_sim_df: pd.DataFrame) -> dict:
    """
    Convert english_sim_df into {word: np.array(20 topic scores)} for
    fast O(1) lookups instead of repeated dataframe merges.
    """
    return {
        row["word"]: row[TOPICS].to_numpy(dtype=np.float32)
        for _, row in english_sim_df.iterrows()
    }


# =====================================================================
# 2. Frequency mapping: attach freq/rank/probs + anchor_word to a
#    target-language dictionary via its direct_translation column
# =====================================================================
def map_frequency_with_anchor(
    lang_df: pd.DataFrame,
    freq_lookup: dict,
    translation_col: str = "direct_translation",
) -> pd.DataFrame:
    """
    lang_df must contain `translation_col` with English translation phrases.
    freq_lookup: {english_word: freq} built from english_sim_df.

    Adds columns: freq, anchor_word, rank, probs.
    - anchor_word = the rarest (lowest-freq) English token in the translation
      phrase — this SAME word is later used to look up topic similarity.
    - probs is renormalized within this language's own matched vocabulary.
    """
    lang_df = lang_df.copy()

    def rarest_freq_and_anchor(phrase):
        if not isinstance(phrase, str) or not phrase.strip():
            return np.nan, None
        tokens = phrase.lower().replace("-", " ").split()
        valid = [(t, freq_lookup[t]) for t in tokens if t in freq_lookup]
        if not valid:
            return np.nan, None
        anchor_word, anchor_freq = min(valid, key=lambda x: x[1])
        return anchor_freq, anchor_word

    result = lang_df[translation_col].apply(rarest_freq_and_anchor)
    lang_df["freq"] = result.apply(lambda x: x[0])
    lang_df["anchor_word"] = result.apply(lambda x: x[1])

    lang_df = lang_df.sort_values(
        "freq", ascending=False, na_position="last"
    ).reset_index(drop=True)
    lang_df["rank"] = np.where(
        lang_df["freq"].notna(), np.arange(1, len(lang_df) + 1), np.nan
    )

    valid_freq_sum = lang_df["freq"].sum()  # NaN skipped by default
    lang_df["probs"] = lang_df["freq"].fillna(0) / valid_freq_sum

    return lang_df


def attach_topic_similarity(
    lang_df: pd.DataFrame,
    sim_lookup: dict,
) -> pd.DataFrame:
    """
    Attach all 20 topic-similarity columns to lang_df via its anchor_word,
    using the fast dict lookup (no merge). Rows with no anchor_word / no
    match get NaN for every topic column.
    """
    lang_df = lang_df.copy()
    n = len(lang_df)
    sim_matrix = np.full((n, len(TOPICS)), np.nan, dtype=np.float32)

    for i, anchor in enumerate(lang_df["anchor_word"].values):
        if anchor in sim_lookup:
            sim_matrix[i] = sim_lookup[anchor]

    for j, topic in enumerate(TOPICS):
        lang_df[topic] = sim_matrix[:, j]

    return lang_df


def prepare_language_dictionary(
    lang_df: pd.DataFrame,
    english_sim_df: pd.DataFrame,
    translation_col: str = "direct_translation",
) -> pd.DataFrame:
    """
    One-call convenience wrapper: freq/rank/probs + anchor_word + all 20
    topic similarity columns, ready for CandidateSelector.
    """
    # Build the freq lookup directly from the similarity DF!
    freq_lookup = dict(zip(english_sim_df["word"], english_sim_df["freq"]))
    sim_lookup = build_similarity_lookup(english_sim_df)

    lang_df = map_frequency_with_anchor(lang_df, freq_lookup, translation_col)
    lang_df = attach_topic_similarity(lang_df, sim_lookup)
    return lang_df
