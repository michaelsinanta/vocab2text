from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path
from typing import List, Mapping, Sequence, Union

from prompt_generation.config import LENGTH_FILES, resolve_language
from .types import FewShotExample, FewShotsByLength, LengthKey

SUPPORTED_FEW_SHOT_LENGTHS = tuple(LENGTH_FILES.values())

_SKIP_MODULES = {"registry", "types", "render"}

FewShotInput = Union[
    str,
    Sequence[FewShotExample],
    Mapping[str, Sequence[FewShotExample]],
]


def normalize_length(length: LengthKey) -> str:
    """Map a length value onto its bucket key."""
    return str(length)


def wrap_flat_few_shots(
    examples: Sequence[FewShotExample],
    *,
    default_length: LengthKey = "5",
) -> FewShotsByLength:
    """Treat a flat list as the pool for a single length bucket."""
    return {normalize_length(default_length): list(examples)}


def get_pool(
    few_shots: FewShotInput,
    sentence_length: LengthKey,
) -> List[FewShotExample]:
    """Return the example pool for the requested length bucket."""
    bucket = normalize_length(sentence_length)
    if isinstance(few_shots, Mapping):
        pool = few_shots.get(bucket)
        if pool is None:
            available = sorted(few_shots.keys(), key=_bucket_sort_key)
            raise KeyError(
                f"No few-shot examples for length '{bucket}'. "
                f"Available buckets: {available}"
            )
        return list(pool)

    if isinstance(few_shots, str):
        raise TypeError(
            "Pre-rendered few-shot strings cannot be filtered by length. "
            "Pass a mapping of length bucket -> examples instead."
        )

    return list(few_shots)


def list_languages() -> List[str]:
    """Language package names under few_shot_prompts/ (sorted)."""
    import few_shot_prompts

    langs = []
    for module in pkgutil.iter_modules(few_shot_prompts.__path__):
        if module.ispkg and module.name not in _SKIP_MODULES:
            langs.append(module.name)
    return sorted(langs)


def load_language_few_shots_by_length(lang: str) -> FewShotsByLength:
    """Load examples from few_shot_prompts/<lang>/{5_words,paragraph,...}.py."""
    lang = resolve_language(lang)
    package_name = f"{__package__}.{lang}"
    try:
        package = importlib.import_module(package_name)
    except ModuleNotFoundError as e:
        available = ", ".join(list_languages()) or "(none)"
        raise SystemExit(
            f"Unknown language '{lang}'. Expected a package at "
            f"few_shot_prompts/{lang}/. Available: {available}"
        ) from e

    package_dir = Path(next(iter(package.__path__)))
    loaded: FewShotsByLength = {}
    for module_name, bucket in LENGTH_FILES.items():
        path = package_dir / f"{module_name}.py"
        if not path.exists():
            continue
        module = importlib.import_module(f"{package_name}.{module_name}")
        if not hasattr(module, "EXAMPLES"):
            raise SystemExit(
                f"{path} must export EXAMPLES (a list of few-shot dicts)."
            )
        loaded[bucket] = list(getattr(module, "EXAMPLES"))

    if not loaded:
        files = ", ".join(f"{name}.py" for name in LENGTH_FILES)
        raise SystemExit(
            f"few_shot_prompts/{lang}/ has no length files. "
            f"Add one of: {files}"
        )
    return loaded


def _bucket_sort_key(bucket: str):
    if bucket == "paragraph":
        return (1, 0)
    try:
        return (0, int(bucket))
    except ValueError:
        return (2, bucket)
