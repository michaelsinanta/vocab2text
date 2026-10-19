"""
Generate prompts using words candidates and few shots examples.

Example:
  python prompt_generation/ours/generate_ours_prompts.py --languages minangkabau --lengths 5_words --topics food travel --samples 100 --seed 42
"""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import argparse
import pandas as pd

from few_shot_prompts.registry import (
    list_languages,
    load_language_few_shots_by_length,
)
from prompt_generation.config import (
    LENGTH_CATEGORIES,
    LENGTH_CLI,
    TOPICS,
    language_display_name,
    resolve_language,
)
from prompt_generation.ours.config import TopicControlledConfig
from prompt_generation.ours.experiment_runner import PromptRunner
from prompt_generation.ours.similarity import (
    load_english_similarity,
    prepare_language_dictionary,
)

DICTIONARY_DIR = REPO_ROOT / "dictionaries"
SIMILARITY_CSV = REPO_ROOT / "english_word_freq" / "english_word_topic_similarity.csv"


def _length_value(bucket: str) -> int:
    return 25 if bucket == "paragraph" else int(bucket)


def generate_rows(
    language: str,
    length_code: str,
    few_shot_length_code: str,
    runner: PromptRunner,
    samples: int,
    topics: list[str],
    n_candidates: int,
    rank_border: int,
    composition: float,
    top_p_similarity: float,
    n_few_shot: int,
    seed: int | None,
    seed_offset: int = 0,
) -> list[dict]:
    category = LENGTH_CATEGORIES[length_code]
    target_bucket = LENGTH_CLI[length_code]
    few_shot_bucket = LENGTH_CLI[few_shot_length_code]
    display_language = language_display_name(language)
    target_length_value = _length_value(target_bucket)
    few_shot_length_value = _length_value(few_shot_bucket)
    config = TopicControlledConfig(
        n_candidates=n_candidates,
        rank_border=rank_border,
        composition=composition,
        top_p_similarity=top_p_similarity,
        target_sentence_length=target_length_value,
        n_few_shot=n_few_shot,
        few_shot_sentence_length=few_shot_length_value,
    )
    prompts = runner.generate_prompts(
        config,
        n_samples=samples,
        seed=None if seed is None else seed + seed_offset,
        topics=topics,
    )
    return [
        {
            **prompt,
            "length_category": category["key"],
            "unit": category["unit"],
            "target_length_desc": category["length_desc"],
            "prompt_type": "few_shots_and_word_candidates",
            "target_sentence_length": target_bucket,
            "n_candidates": n_candidates,
            "rank_border": rank_border,
            "composition": composition,
            "top_p_similarity": top_p_similarity,
            "n_few_shot": n_few_shot,
            "few_shot_sentence_length": few_shot_bucket,
        }
        for prompt in prompts
    ]


def save(df: pd.DataFrame, out_dir: Path, split_by: str, base_name: str | None):
    if split_by == "none":
        groups = [(base_name or "ours_prompts", df)]
    elif split_by == "language":
        groups = [
            (f"{language.lower()}_ours", group)
            for language, group in df.groupby("language")
        ]
    elif split_by == "length":
        groups = [
            (f"{length}_ours", group) for length, group in df.groupby("length_category")
        ]
    else:
        groups = [
            (f"{language.lower()}_{length}_ours", group)
            for (language, length), group in df.groupby(["language", "length_category"])
        ]

    for name, group in groups:
        path = out_dir / f"{name}.csv"
        group.to_csv(path, index=False, encoding="utf-8")
        print(f"Saved {len(group)} prompts -> {path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--languages",
        nargs="+",
        default=["minangkabau"],
        help="Language names with dictionary and few-shot data (default: minangkabau)",
    )
    parser.add_argument(
        "--lengths",
        nargs="+",
        choices=list(LENGTH_CATEGORIES),
        default=["5_words"],
        help="Target output lengths (default: 5_words)",
    )
    parser.add_argument(
        "--few-shot-length",
        choices=list(LENGTH_CATEGORIES),
        default=None,
        help="Few-shot example bucket (default: use each target length)",
    )
    parser.add_argument(
        "--topics",
        nargs="+",
        choices=TOPICS,
        default=None,
        help="Topics to cycle through (default: all configured topics)",
    )
    parser.add_argument("--samples", type=int, default=100)
    parser.add_argument("--n-candidates", type=int, default=300)
    parser.add_argument("--rank-border", type=int, default=500)
    parser.add_argument("--composition", type=float, default=0.1)
    parser.add_argument("--top-p-similarity", type=float, default=0.25)
    parser.add_argument("--n-few-shot", type=int, default=3)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument(
        "--split-by",
        choices=["none", "language", "length", "language-length"],
        default="language",
    )
    parser.add_argument("--output-dir", default="./outputs/ours")
    parser.add_argument(
        "--output-name",
        default=None,
        help="Base filename; only used with --split-by none",
    )
    parser.add_argument(
        "--similarity-csv",
        type=Path,
        default=SIMILARITY_CSV,
        help="English frequency/topic-similarity CSV",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List languages, lengths, and topics",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.list:
        languages = [
            language
            for language in list_languages()
            if (DICTIONARY_DIR / f"{language}.csv").is_file()
        ]
        print("Languages:", ", ".join(languages) or "(none)")
        print("Lengths:  ", ", ".join(LENGTH_CATEGORIES))
        print("Topics:   ", ", ".join(TOPICS))
        return

    if args.samples < 0:
        parser.error("--samples must be zero or greater")
    if args.n_candidates <= 0:
        parser.error("--n-candidates must be greater than zero")
    if args.rank_border <= 0:
        parser.error("--rank-border must be greater than zero")
    if args.n_few_shot < 0:
        parser.error("--n-few-shot must be zero or greater")
    if not 0 < args.composition <= 1:
        parser.error("--composition must be greater than 0 and at most 1")
    if not 0 < args.top_p_similarity <= 1:
        parser.error("--top-p-similarity must be greater than 0 and at most 1")

    languages = list_languages()
    language_lookup = {language.lower(): language for language in languages}
    selected_languages = []
    for value in args.languages:
        language = language_lookup.get(resolve_language(value))
        if language is None:
            parser.error(
                f"Unknown language '{value}'. Available: {', '.join(languages)}"
            )
        if not (DICTIONARY_DIR / f"{language}.csv").is_file():
            parser.error(f"Missing dictionary: {DICTIONARY_DIR / f'{language}.csv'}")
        if language not in selected_languages:
            selected_languages.append(language)

    topic_list = args.topics or TOPICS
    few_shot_length_codes = [
        args.few_shot_length or length_code for length_code in args.lengths
    ]
    similarity_df = load_english_similarity(args.similarity_csv)
    all_rows = []
    seed_offset = 0

    for language in selected_languages:
        language_few_shots = load_language_few_shots_by_length(language)
        dictionary = pd.read_csv(DICTIONARY_DIR / f"{language}.csv")
        enriched_dictionary = prepare_language_dictionary(dictionary, similarity_df)
        display_language = language_display_name(language)
        runner = PromptRunner(
            enriched_dictionary, language_few_shots, display_language
        )

        for length_code, few_shot_length_code in zip(
            args.lengths, few_shot_length_codes
        ):
            bucket = LENGTH_CLI[few_shot_length_code]
            if bucket not in language_few_shots:
                print(
                    f"Skipping {language}/{length_code}: no few-shot examples "
                    f"for {few_shot_length_code}."
                )
                continue
            rows = generate_rows(
                language=language,
                length_code=length_code,
                few_shot_length_code=few_shot_length_code,
                runner=runner,
                samples=args.samples,
                topics=topic_list,
                n_candidates=args.n_candidates,
                rank_border=args.rank_border,
                composition=args.composition,
                top_p_similarity=args.top_p_similarity,
                n_few_shot=args.n_few_shot,
                seed=args.seed,
                seed_offset=seed_offset,
            )
            seed_offset += args.samples
            print(
                f"Generated {len(rows)} topic-controlled prompts for "
                f"{language}/{length_code}"
            )
            all_rows.extend(rows)

    if not all_rows:
        raise SystemExit("No prompts generated.")

    out_dir = Path(args.output_dir)
    if not out_dir.is_absolute():
        out_dir = Path.cwd() / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    save(pd.DataFrame(all_rows), out_dir, args.split_by, args.output_name)


if __name__ == "__main__":
    main()
