"""Shared language, length, and topic lists for every prompt type.

ours, few-shot, and zero-shot CLIs all import from here. Few-shot example
files use ``LENGTH_FILES`` (e.g. ``5_words.py``, ``paragraph.py``).
"""

from typing import Dict, List

# Language names, all lowercase (e.g. "minangkabau").
# Keep this name identical everywhere the language appears:
#   LANGUAGES            -> "minangkabau"
#   few_shot_prompts/    -> minangkabau/    (folder, must be a valid Python package)
#   dictionaries/        -> minangkabau.csv
#   --languages flag     -> minangkabau     (case-insensitive)
# See "Adding a new language" in README.md.
LANGUAGES: List[str] = [
    "hitu",
    "indonesian",
    "javanese",
    "minangkabau",
    "vietnamese",
    "acehnese",
]

# CLI flag -> metadata. ``key`` is the few-shot filename stem.
LENGTH_CATEGORIES = {
    "5_words": {
        "key": "5_words",
        "bucket": "5",
        "unit": "sentence",
        "length_desc": "5 words",
    },
    "10_words": {
        "key": "10_words",
        "bucket": "10",
        "unit": "sentence",
        "length_desc": "10 words",
    },
    "15_words": {
        "key": "15_words",
        "bucket": "15",
        "unit": "sentence",
        "length_desc": "15 words",
    },
    "20_words": {
        "key": "20_words",
        "bucket": "20",
        "unit": "sentence",
        "length_desc": "20 words",
    },
    "paragraph": {
        "key": "paragraph",
        "bucket": "paragraph",
        "unit": "paragraph",
        "length_desc": "contains at least 3 sentences and at least 25 words",
    },
}

# few_shot_prompts/<lang>/<file>.py -> bucket key
LENGTH_FILES: Dict[str, str] = {
    cat["key"]: cat["bucket"] for cat in LENGTH_CATEGORIES.values()
}

PARAGRAPH_BUCKET = "paragraph"

LENGTH_CLI: Dict[str, str] = {
    code: cat["bucket"] for code, cat in LENGTH_CATEGORIES.items()
}

TOPICS: List[str] = [
    "food",
    "family",
    "holiday",
    "travel",
    "health",
    "fitness",
    "education",
    "technology",
    "music",
    "movies",
    "books",
    "fashion",
    "nature",
    "pets",
    "business",
    "art",
    "science",
    "gaming",
    "home",
    "garden",
]


def resolve_language(value: str) -> str:
    return value.strip().lower()


def language_display_name(value: str) -> str:
    slug = resolve_language(value)
    for name in LANGUAGES:
        if name.lower() == slug:
            return name
    return slug.capitalize()


def bucket_filename(bucket: str) -> str:
    for module_name, key in LENGTH_FILES.items():
        if key == bucket:
            return f"{module_name}.py"
    return f"{bucket}.py"
