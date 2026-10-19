"""Per-language few-shot example libraries.

Layout::

    few_shot_prompts/
      <language>/
        5_words.py
        10_words.py
        15_words.py
        20_words.py
        paragraph.py   # optional

Each length file exports ``EXAMPLES``, a list of ``FewShotExample`` dicts.

To add a language, create its folder with the length files you need.
To add a few-shot, append a dict to ``EXAMPLES`` in the matching file.
"""

from prompt_generation.config import LENGTH_FILES

from .registry import (
    get_pool,
    list_languages,
    load_language_few_shots_by_length,
    normalize_length,
)

__all__ = [
    "LENGTH_FILES",
    "get_pool",
    "list_languages",
    "load_language_few_shots_by_length",
    "normalize_length",
]
