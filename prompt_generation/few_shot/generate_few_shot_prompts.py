"""
Generate few-shot-only prompts.

Example:
  python prompt_generation/few_shot/generate_few_shot_prompts.py --languages minangkabau --lengths 5_words --samples 100
  python prompt_generation/few_shot/generate_few_shot_prompts.py --languages minangkabau indonesian --lengths 5_words 10_words paragraph --seed 42
  python prompt_generation/few_shot/generate_few_shot_prompts.py --list
"""

from pathlib import Path
import sys

# `python this_file.py` puts this folder on sys.path, not the repo.
# `python -m prompt_generation.few_shot` already has the repo root.
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import argparse
import uuid

from few_shot_prompts.registry import (
    list_languages,
    load_language_few_shots_by_length,
)
from prompt_generation.config import (
    LENGTH_CLI,
    LENGTH_CATEGORIES,
    bucket_filename,
    language_display_name,
    resolve_language,
)
from prompt_generation.few_shot.config import ExperimentConfig
from prompt_generation.few_shot.prompt_generator import FewShotPromptGenerator


# ---------------------------------------------------------------- generation
def generate_rows(language, length_code, pool, samples, n_few_shot, seed):
    category = LENGTH_CATEGORIES[length_code]
    target_len = LENGTH_CLI[length_code]
    config = ExperimentConfig(
        exp_id=f"FS_{language[:3].upper()}_{length_code}",
        target_sentence_length=target_len,
        n_few_shot=n_few_shot,
        few_shot_sentence_length=target_len,
    )
    generator = FewShotPromptGenerator(pool, target_language=language)

    rows = []
    for i in range(samples):
        sample_seed = None if seed is None else seed + i
        prompt, _few_shot_text = generator.generate_prompt_few_shots_only(
            config, seed=sample_seed
        )
        rows.append(
            {
                "prompt_id": str(uuid.uuid4()),
                "language": language_display_name(language),
                "length_category": category["key"],
                "unit": category["unit"],
                "target_length_desc": category["length_desc"],
                "prompt_type": "few_shots_only",
                "target_sentence_length": target_len,
                "n_few_shot": n_few_shot,
                "few_shot_sentence_length": target_len,
                "prompt": prompt,
            }
        )
    return rows


def write(df, path):
    df.to_csv(path.with_suffix(".csv"), index=False, encoding="utf-8")
    print(f"Saved {len(df)} prompts -> {path.with_suffix('.csv')}")


def save(df, out_dir, split_by, base_name):
    if split_by == "none":
        groups = [(base_name or "few_shot_prompts", df)]
    elif split_by == "language":
        groups = [(f"{lang.lower()}_few_shot", g) for lang, g in df.groupby("language")]
    else:  # language-length
        groups = [
            (f"{lang.lower()}_{ln}_few_shot", g)
            for (lang, ln), g in df.groupby(["language", "length_category"])
        ]
    for name, g in groups:
        write(g, out_dir / name)


# === CLI ====
def list_available():
    print("Languages:", ", ".join(list_languages()) or "(none)")
    print("Lengths:  ", ", ".join(f"{k}={v}" for k, v in LENGTH_CLI.items()))
    for lang in list_languages():
        buckets = sorted(
            load_language_few_shots_by_length(lang).keys(),
            key=lambda b: (
                (1, 0) if b == "paragraph" else (0, int(b) if b.isdigit() else 99)
            ),
        )
        print(f"  {lang}: {', '.join(buckets)}")


def build_parser():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument(
        "--languages",
        nargs="+",
        default=["minangkabau"],
        help="Language names (default: minangkabau)",
    )
    p.add_argument(
        "--lengths",
        nargs="+",
        default=["5_words"],
        choices=list(LENGTH_CLI),
        help="Length categories (default: 5_words)",
    )
    p.add_argument(
        "--samples",
        type=int,
        default=100,
        help="Prompts per language x length (default: 100)",
    )
    p.add_argument(
        "--n-few-shot",
        type=int,
        default=3,
        help="Few-shot examples per prompt (default: 3)",
    )
    p.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Base seed; sample i uses seed+i (default: not reproducible)",
    )
    p.add_argument(
        "--split-by",
        default="language",
        choices=["none", "language", "language-length"],
        help="How to split output files (default: language)",
    )
    p.add_argument("--output-dir", default="./outputs/few_shot")
    p.add_argument(
        "--output-name",
        default=None,
        help="Base filename; only used with --split-by none",
    )
    p.add_argument(
        "--list", action="store_true", help="List available languages/lengths and exit"
    )
    return p


def main():
    args = build_parser().parse_args()

    if args.list:
        list_available()
        return

    all_rows = []
    for lang_arg in args.languages:
        language = resolve_language(lang_arg)
        try:
            pool = load_language_few_shots_by_length(language)
        except SystemExit as e:
            print(e)
            continue
        for length_code in args.lengths:
            bucket = LENGTH_CLI[length_code]
            try:
                rows = generate_rows(
                    language,
                    length_code,
                    pool,
                    args.samples,
                    args.n_few_shot,
                    args.seed,
                )
            except KeyError:
                print(
                    f"Skipping {language}/{length_code}: no few-shot file "
                    f"few_shot_prompts/{language}/{bucket_filename(bucket)}"
                )
                continue
            except ValueError as e:
                print(f"Skipping {language}/{length_code}: {e}")
                continue
            print(f"Generated {len(rows)} prompts for {language}/{length_code}")
            all_rows.extend(rows)

    if not all_rows:
        raise SystemExit("No prompts generated.")

    out_dir = Path(args.output_dir)
    if not out_dir.is_absolute():
        out_dir = Path.cwd() / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    import pandas as pd

    save(pd.DataFrame(all_rows), out_dir, args.split_by, args.output_name)


if __name__ == "__main__":
    main()
