"""
Generate topic-related zero-shot prompts for text generation.
"""

from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import argparse
import uuid

from prompt_generation.config import (
    LANGUAGES,
    LENGTH_CATEGORIES,
    TOPICS,
    language_display_name,
)

# ===== PROMPT =====


def build_topic_related_prompt(language, unit, length_desc, topic):
    if unit == "paragraph":
        length_clause = f"Ensure that the {unit} {length_desc}. "
    else:
        length_clause = f"Ensure that the {unit} is around {length_desc} long. "

    return (
        f"Generate a {unit} in the {language} language about {topic}. "
        f"{length_clause}"
        f"Return only the {unit}."
    )


def generate_rows(languages, lengths, topics, samples):
    rows = []
    for language in languages:
        for length_code in lengths:
            cat = LENGTH_CATEGORIES[length_code]
            for i in range(samples):
                topic = topics[i % len(topics)]
                rows.append(
                    {
                        "prompt_id": str(uuid.uuid4()),
                        "language": language_display_name(language),
                        "topic": topic,
                        "prompt": build_topic_related_prompt(
                            language, cat["unit"], cat["length_desc"], topic
                        ),
                        "length_category": cat["key"],
                        "unit": cat["unit"],
                        "target_length_desc": cat["length_desc"],
                        "prompt_type": "topic_related",
                    }
                )
    return rows


# ===== CLI =====


def parse_languages(values):
    """Accept registered language names, case-insensitively."""
    names_by_lowercase = {name.lower(): name for name in LANGUAGES}
    result = {}
    for v in values:
        name = names_by_lowercase.get(v.strip().lower())
        if name is not None:
            result[name] = name
        else:
            raise SystemExit(
                f"Unknown language '{v}'. Use a language name: "
                f"{', '.join(LANGUAGES)}."
            )
    return list(result.values())


def build_parser():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument(
        "--languages",
        nargs="+",
        default=["Minangkabau"],
        help="Language names (default: Minangkabau)",
    )
    p.add_argument(
        "--lengths",
        nargs="+",
        default=["5_words"],
        choices=list(LENGTH_CATEGORIES),
        help="Length categories (default: 5_words)",
    )
    p.add_argument(
        "--topics", nargs="+", default=None, help="Subset of topics (default: all)"
    )
    p.add_argument(
        "--samples",
        type=int,
        default=1000,
        help="Prompts per language x length (default: 1000)",
    )
    p.add_argument(
        "--split-by",
        default="language",
        choices=["none", "language", "length", "language-length"],
        help="How to split output files (default: language)",
    )
    p.add_argument("--output-dir", default="./outputs/zero_shot")
    p.add_argument(
        "--output-name",
        default=None,
        help="Base filename; only used with --split-by none (default: prompts)",
    )
    p.add_argument(
        "--list",
        action="store_true",
        help="List available languages, lengths, topics and exit",
    )
    return p


def save(df, out_dir, split_by, base_name):
    if split_by == "none":
        groups = [(base_name or "prompts", df)]
    elif split_by == "language":
        groups = [
            (f"{lang.lower()}_zero_shot", g) for lang, g in df.groupby("language")
        ]
    elif split_by == "length":
        groups = [(f"{ln}_zero_shot", g) for ln, g in df.groupby("length_category")]
    else:
        groups = [
            (f"{lang.lower()}_{ln}_zero_shot", g)
            for (lang, ln), g in df.groupby(["language", "length_category"])
        ]

    for name, g in groups:
        path = out_dir / f"{name}.csv"
        g.to_csv(path, index=False, encoding="utf-8")
        print(f"Saved {len(g)} prompts -> {path}")


def main():
    args = build_parser().parse_args()

    if args.list:
        print("Languages:", ", ".join(LANGUAGES))
        print("Lengths:  ", ", ".join(LENGTH_CATEGORIES))
        print("Topics:   ", ", ".join(TOPICS))
        return

    languages = parse_languages(args.languages)
    topics = args.topics or TOPICS

    import pandas as pd

    df = pd.DataFrame(generate_rows(languages, args.lengths, topics, args.samples))
    print(f"Generated {len(df)} prompts.")

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    save(df, out_dir, args.split_by, args.output_name)


if __name__ == "__main__":
    main()
