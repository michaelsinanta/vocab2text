from __future__ import annotations

import argparse
from typing import Sequence

from .registry import (
    SUPPORTED_FEW_SHOT_LENGTHS,
    get_pool,
    load_language_few_shots_by_length,
)
from .types import FewShotExample, LengthKey


def infer_few_shots(examples: Sequence[FewShotExample], n: int) -> str:
    if n <= 0 or not examples:
        return ""

    selected = list(examples)[:n]

    formatted_parts: list[str] = []
    for i, ex in enumerate(selected, 1):
        part = f"Example {i}\n\n"
        part += f"Word Candidates:\n{ex['word_candidates']}\n\n"
        part += f"Output:\n{ex['output']}"
        formatted_parts.append(part)

    return "\n\n".join(formatted_parts)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render few-shot examples from few_shot_prompts/<language>/."
    )
    parser.add_argument(
        "--lang",
        required=True,
        help="Language folder name (e.g. indonesian, minangkabau, acehnese).",
    )
    parser.add_argument(
        "--n",
        type=int,
        default=3,
        help="Number of examples to render (default: 3). Use -1 for all.",
    )
    parser.add_argument(
        "--length",
        default="5",
        help="Length bucket: 5, 10, 15, 20, or paragraph. Default: 5.",
    )
    return parser


def _parse_length(value: str) -> LengthKey:
    raw = value.strip().lower()
    if raw in SUPPORTED_FEW_SHOT_LENGTHS:
        return raw
    try:
        return int(raw)
    except ValueError:
        return raw


if __name__ == "__main__":
    args = _build_parser().parse_args()
    by_length = load_language_few_shots_by_length(args.lang)
    examples = get_pool(by_length, _parse_length(args.length))
    n = len(examples) if args.n < 0 else args.n
    rendered = infer_few_shots(examples, n)
    print(rendered)
