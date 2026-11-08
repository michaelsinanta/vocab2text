# Text Generation in Low-Resource Languages Using Human-Curated Vocabularies

Code for the paper **[Text Generation in Low-Resource Languages Using Human-Curated Vocabularies](https://arxiv.org/abs/2610.37105v1)**.

This repository builds the **prompts** used to ask a large language model to write text in a low-resource language. It does not call any model itself: it writes CSV files of ready-to-use prompts.

## Which prompts to generate

There are three prompt types. Each one has its own section below with its own options, requirements, and output.

| Prompt type                      | Command                                 | What the prompt contains                                                                                         | Role                                 |
| -------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| [Ours](#ours-paper-method)       | `python -m prompt_generation.ours`      | Task instructions, few-shot examples, and a **list of candidate words** (POS, English meaning, example sentence) | Paper method — use this to replicate |
| [Few-shot](#few-shot-baseline)   | `python -m prompt_generation.few_shot`  | Task instructions + a few human-written example outputs (no dictionary candidates)                               | Baseline used in the paper           |
| [Zero-shot](#zero-shot-baseline) | `python -m prompt_generation.zero_shot` | A short instruction to write about a topic at a given length (no examples, no dictionary)                        | Baseline used in the paper           |

If you want to **replicate the method from the paper**, generate **ours**. Few-shot and zero-shot are the baselines we compared against, not the method to replicate.

Each prompt asks for one sentence (about 5, 10, 15, or 20 words) or one paragraph.

## Repository structure

```
.
├── prompt_generation/        # all prompt-building code
│   ├── config.py             # shared: languages, length categories, topics
│   ├── ours/                 # paper method
│   ├── few_shot/             # few-shot baseline
│   └── zero_shot/            # zero-shot baseline
├── few_shot_prompts/         # hand-written examples, one folder per language
│   └── <language>/
│       ├── __init__.py       # required: makes the folder a Python package
│       └── 5_words.py, 10_words.py, 15_words.py, 20_words.py, paragraph.py
├── dictionaries/             # <language>.csv: human-curated dictionary per language
├── english_word_freq/        # english_word_topic_similarity.csv
├── outputs/                  # generated prompt CSVs (not tracked in git)
└── requirements.txt          # pip install -r requirements.txt
```

## Setup

```bash
pip install -r requirements.txt
```

This installs `pandas` and `numpy`, the only third-party packages the code needs.

Run all commands from the **repository root** as modules (`python -m ...`). That puts the repo on Python's import path, so you do not need extra `sys.path` setup.

## Shared settings

All three prompt types read the same lists from `prompt_generation/config.py`:

- **Languages** (`LANGUAGES`): see [Adding a new language](#adding-a-new-language).
- **Length buckets**: `5_words`, `10_words`, `15_words`, `20_words` (one sentence of about that many words) and `paragraph` (at least 3 sentences and at least 25 words).
- **Topics** (`TOPICS`): food, family, holiday, travel, health, fitness, education, technology, music, movies, books, fashion, nature, pets, business, art, science, gaming, home, garden.

---

## Ours (paper method)

This is the main method of the paper. Each prompt gives the model task instructions, a few human-written few-shot examples, and a list of candidate words taken from a human-curated dictionary, then asks it to write one sentence or paragraph.

### What the prompt contains

1. Task instructions (vocabulary, punctuation, length, quality, and originality rules).
2. `--n-few-shot` few-shot examples. Each one shows a "Word Candidates" list and the human-written output. The example's own words are kept, and the list is padded with random dictionary words up to `--n-candidates`, so the examples look like the real prompt.
3. The **candidate list** for the new text: `word | part of speech | English meaning | example sentence`, one word per line.
4. The topic for the text, when one is set.

### How the candidate list is sampled

The list is built so that it is:

1. **Frequency-aware.** Target-language words have no frequency data, so each one borrows the frequency of the rarest word in its English translation (the "anchor word"). Words are then ranked by that frequency within the language's dictionary.
2. **Topic-controlled.** A fraction of the candidates (`--composition`) are common words, drawn from the words ranked at or above `--rank-border`. The rest are rarer words: only the `--top-p-similarity` share most related to the chosen topic is kept, and the remaining slots are sampled from it. If either pool runs short, the list is topped up with other valid words.

### Requirements

- `dictionaries/<language>.csv`
- `few_shot_prompts/<language>/` with the length files you want to generate
- `english_word_freq/english_word_topic_similarity.csv`

A language and length that has no few-shot examples is skipped with a `Skipping ...` message.

### Run

```bash
python -m prompt_generation.ours \
  --languages minangkabau --lengths 5_words --topics food travel \
  --samples 100 --seed 42
```

Writes CSVs under `./outputs/ours` by default. `python -m prompt_generation.ours --list` shows the languages that have a dictionary, the length buckets, and the topics.

### Options

| Option               | Default                                               | Meaning                                                                                   |
| -------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `--languages`        | `minangkabau`                                         | Languages to generate for. Each needs a dictionary and a few-shot folder                  |
| `--lengths`          | `5_words`                                             | Target output length(s): `5_words`, `10_words`, `15_words`, `20_words`, `paragraph`       |
| `--few-shot-length`  | same as target                                        | Which length bucket to draw few-shot examples from (same value for every target length)   |
| `--topics`           | all topics                                            | Topics to cycle through (must be topics from `config.py`)                                 |
| `--samples`          | 100                                                   | Prompts per language and length                                                           |
| `--n-candidates`     | 300                                                   | Number of candidate words in each prompt                                                  |
| `--rank-border`      | 500                                                   | Words ranked at or above this (rank number at or below it) count as high-frequency        |
| `--composition`      | 0.1                                                   | Fraction of candidates drawn from the high-frequency pool (greater than 0, at most 1)     |
| `--top-p-similarity` | 0.25                                                  | Share of low-frequency words kept, ranked by topic similarity (greater than 0, at most 1) |
| `--n-few-shot`       | 3                                                     | Few-shot examples per prompt                                                              |
| `--seed`             | none                                                  | Base seed; sample _i_ uses `seed + i` for reproducibility                                 |
| `--similarity-csv`   | `english_word_freq/english_word_topic_similarity.csv` | English frequency / topic-similarity CSV                                                  |
| `--split-by`         | `language`                                            | Output split: `none`, `language`, `length`, `language-length`                             |
| `--output-dir`       | `./outputs/ours`                                      | Where CSVs are written                                                                    |
| `--output-name`      | `ours_prompts`                                        | Base file name; only used with `--split-by none`                                          |
| `--list`             | off                                                   | List languages, lengths, and topics, then exit                                            |

### Output

Files are named `<language>_ours.csv` (`--split-by language`), `<length>_ours.csv` (`length`), `<language>_<length>_ours.csv` (`language-length`), or `<output-name>.csv` (`none`).

Each row is one prompt, with these columns:

- `prompt_id`, `language`, `topic`, `prompt`, `prompt_type` (`few_shots_and_word_candidates`)
- `length_category`, `unit`, `target_length_desc`, `target_sentence_length`, `few_shot_sentence_length`
- `seed`, `candidate_seed` (the seeds that reproduce the sample and its candidate list)
- the sampling settings: `n_candidates`, `rank_border`, `composition`, `top_p_similarity`, `n_few_shot`
- `n_candidates_actual` (candidates actually selected) and `n_few_shot_used` (examples actually shown)

---

## Few-shot baseline

A baseline from the paper. Each prompt gives the model task instructions and a few human-written example outputs, then asks for one sentence or paragraph. It has **no dictionary candidates and no topic**.

### What the prompt contains

1. Task instructions (few-shot guidance, punctuation, length, and quality rules).
2. `--n-few-shot` example outputs, listed as `Example 1: ...`, `Example 2: ...`. Only the human-written outputs are shown, not their word lists.

The examples are sampled at random from the language's examples for the same length as the target. With `--seed`, sample _i_ uses `seed + i`, so results are reproducible.

### Requirements

- `few_shot_prompts/<language>/` with the length files you want to generate

It does not use the dictionary.

### Run

```bash
python -m prompt_generation.few_shot \
  --languages minangkabau --lengths 5_words --samples 100 --seed 42
```

Writes CSVs under `./outputs/few_shot` by default. `python -m prompt_generation.few_shot --list` shows the languages and which length buckets each has examples for.

### Options

| Option          | Default              | Meaning                                                                             |
| --------------- | -------------------- | ----------------------------------------------------------------------------------- |
| `--languages`   | `minangkabau`        | Languages to generate for. Each needs a folder under `few_shot_prompts/`            |
| `--lengths`     | `5_words`            | Target output length(s): `5_words`, `10_words`, `15_words`, `20_words`, `paragraph` |
| `--samples`     | 100                  | Prompts per language and length                                                     |
| `--n-few-shot`  | 3                    | Few-shot examples per prompt                                                        |
| `--seed`        | none                 | Base seed; sample _i_ uses `seed + i` for reproducibility                           |
| `--split-by`    | `language`           | Output split: `none`, `language`, `language-length`                                 |
| `--output-dir`  | `./outputs/few_shot` | Where CSVs are written                                                              |
| `--output-name` | `few_shot_prompts`   | Base file name; only used with `--split-by none`                                    |
| `--list`        | off                  | List available languages and length buckets, then exit                              |

There is no `--topics` option and no `--split-by length`. The few-shot examples always come from the same length as the target.

### Output

Files are named `<language>_few_shot.csv` (`--split-by language`), `<language>_<length>_few_shot.csv` (`language-length`), or `<output-name>.csv` (`none`).

Each row is one prompt, with these columns: `prompt_id`, `language`, `prompt`, `prompt_type` (`few_shots_only`), `length_category`, `unit`, `target_length_desc`, `target_sentence_length`, `few_shot_sentence_length`, and `n_few_shot`.

---

## Zero-shot baseline

A baseline from the paper. Each prompt is a single short instruction that names the language, length, and a topic. It has **no few-shot examples and no dictionary**.

### What the prompt contains

One sentence of instruction, for example:

> Generate a sentence in the minangkabau language about food. Ensure that the sentence is around 5 words long. Return only the sentence.

For `paragraph`, the length part reads "Ensure that the paragraph contains at least 3 sentences and at least 25 words."

Topics are cycled through the prompts in order, so the samples are spread evenly across the topics you pass.

### Requirements

- The language must be listed in `LANGUAGES` in `prompt_generation/config.py`.

It does not use the dictionary or the few-shot files.

### Run

```bash
python -m prompt_generation.zero_shot \
  --languages minangkabau --lengths 5_words --topics food travel --samples 100
```

Writes CSVs under `./outputs/zero_shot` by default. `python -m prompt_generation.zero_shot --list` shows the languages, lengths, and topics.

### Options

| Option          | Default               | Meaning                                                                             |
| --------------- | --------------------- | ----------------------------------------------------------------------------------- |
| `--languages`   | `minangkabau`         | Languages to generate for (names from `LANGUAGES` in `config.py`)                   |
| `--lengths`     | `5_words`             | Target output length(s): `5_words`, `10_words`, `15_words`, `20_words`, `paragraph` |
| `--topics`      | all topics            | Topics to cycle through                                                             |
| `--samples`     | 1000                  | Prompts per language and length                                                     |
| `--split-by`    | `language`            | Output split: `none`, `language`, `length`, `language-length`                       |
| `--output-dir`  | `./outputs/zero_shot` | Where CSVs are written                                                              |
| `--output-name` | `prompts`             | Base file name; only used with `--split-by none`                                    |
| `--list`        | off                   | List available languages, lengths, and topics, then exit                            |

There is no `--seed` option, and the default `--samples` is 1000, not 100.

### Output

Files are named `<language>_zero_shot.csv` (`--split-by language`), `<length>_zero_shot.csv` (`length`), `<language>_<length>_zero_shot.csv` (`language-length`), or `<output-name>.csv` (`none`).

Each row is one prompt, with these columns: `prompt_id`, `language`, `topic`, `prompt`, `prompt_type` (`topic_related`), `length_category`, `unit`, and `target_length_desc`.

---

## Adding a new language

Adding a language takes four steps: pick a name, add the dictionary, add few-shot examples, and register the name in the config. The **ours** and **few-shot** generators need the few-shot examples, so do not skip step 3.

### 1. Pick one name and use it everywhere

Choose a **single word, letters only** (no spaces, hyphens, or underscores), for example `banjar`. The same name must appear in every place below. Use lowercase for all of them.

| Where                                        | Value for `banjar`         |
| -------------------------------------------- | -------------------------- |
| `LANGUAGES` in `prompt_generation/config.py` | `"banjar"`                 |
| Few-shot folder                              | `few_shot_prompts/banjar/` |
| Dictionary file                              | `dictionaries/banjar.csv`  |
| `--languages` flag (case-insensitive)        | `--languages banjar`       |

The generators lowercase whatever you pass to `--languages` and use that as the folder and CSV name, so a mismatch (for example `few_shot_prompts/Banjar/` or `dictionaries/banjar_dict.csv`) shows up as "Unknown language" or "Missing dictionary".

### 2. Add the dictionary

Create `dictionaries/<language>.csv` with the columns `word`, `direct_translation`, `pos_mapped`, `meaning_translated`, and `example`. Only **ours** reads it.

### 3. Add the few-shot examples

After the dictionary, add few-shot examples for the language under `few_shot_prompts/<language>/`. Create these six files:

```
few_shot_prompts/<language>/
├── __init__.py      # can contain just a docstring, but the file must exist
├── 5_words.py
├── 10_words.py
├── 15_words.py
├── 20_words.py
└── paragraph.py
```

`__init__.py` is required. Without it the language is not detected and `--list` will not show it.

Each length file defines one list called `EXAMPLES`. Copy an existing language (for example `few_shot_prompts/minangkabau/5_words.py`) and replace the content. Every entry has the same three keys:

```python
"""5-word few-shot examples for banjar."""
from __future__ import annotations

from typing import List

from ..types import FewShotExample

EXAMPLES: List[FewShotExample] = [
    {
        "word_candidates": "\n".join(
            [
                "<word> | <part of speech> | <English meaning> | <example sentence or N/A>",
                "<word> | <part of speech> | <English meaning> | N/A",
                # ... one line per word
            ]
        ),
        "output": "The human-written sentence in the target language.",
        "translation": "English translation of the output.",
    },
    # ... more examples
]
```

| Key               | What to put                                                                                                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `word_candidates` | The words the output needs, one per line, as `word \| pos \| English meaning \| example` (use `N/A` when there is no example). This is the same format as the candidate list in the real prompt. |
| `output`          | The natural, human-written text in the target language. It must match the length bucket of its file.                                                                                             |
| `translation`     | The English translation of `output`.                                                                                                                                                             |

What the existing languages follow, and what you should match:

- **One file per length bucket.** `5_words.py`, `10_words.py`, `15_words.py`, `20_words.py` hold sentences of about that many words. `paragraph.py` holds paragraphs of at least 3 sentences and at least 25 words.
- **How many examples.** The existing languages have about 10 examples in each sentence file and 5 in `paragraph.py`. The prompt uses `--n-few-shot` examples (default 3), so each file needs at least that many, and more gives the generator variety to sample from.
- **Candidate lines.** Include every word that `output` uses, each in the dictionary's `word | pos | meaning | example` form. In **ours**, the generator keeps these lines as they are and pads each example with extra random dictionary words, so the words you list are the ones that matter. Take them from your `dictionaries/<language>.csv` so they match what the model sees in the real prompt.
- **Part-of-speech labels.** Reuse the labels already in the dictionary (`noun`, `verb`, `adjective`, `adverb`, `pronoun`, `preposition`, `conjunction`, `proper noun`, ...).
- **Originality.** Write the examples about varied, everyday topics. The prompt tells the model not to reuse their content.
- **Missing files.** A missing length file is skipped when loading, but you cannot generate that length. **Ours** prints `Skipping <language>/<length>: no few-shot examples for ...` and writes nothing for it, and the few-shot generator reports "No few-shot examples for length ...". Provide all five files, or only request the lengths you have (`--lengths` and, for ours, `--few-shot-length`).

Check what you wrote:

```bash
# Render the first 2 examples of a length bucket as they appear in the prompt.
# Use the bucket name here: 5, 10, 15, 20, or paragraph (not 5_words).
python -m few_shot_prompts.render --lang <language> --length 5 --n 2

# The language and its length buckets should be listed.
python -m prompt_generation.few_shot --list
```

### 4. Register the name in the config

Add the lowercase name to `LANGUAGES` in `prompt_generation/config.py`:

```python
LANGUAGES: List[str] = [
    "hitu",
    "indonesian",
    "javanese",
    "minangkabau",
    "vietnamese",
    "acehnese",
    "banjar",   # <- new language, same spelling as the folder and CSV
]
```

The config name controls how the language appears inside the prompt text and the `language` column of the output CSVs. The **zero-shot** generator only accepts names listed here, and without an entry the other generators fall back to a plain `.capitalize()` of the folder name.

### 5. Generate

```bash
python -m prompt_generation.ours --list        # shows languages that have both a dictionary and few-shot files
python -m prompt_generation.ours --languages banjar --lengths 5_words --samples 10 --seed 42
```

## Citation

If you use this code, please cite:

```bibtex
@misc{sinanta2026textgenerationlowresourcelanguages,
      title={Text Generation in Low-Resource Languages Using Human-Curated Vocabularies},
      author={Michael Christlambert Sinanta and Muhammad Dehan Al Kautsar and Amanda Nurul Izzah and Thanh-Nhi Nguyen and Phan Phuong Mai Chau and Zheng Wei Lim and Fajri Koto},
      year={2026},
      eprint={2610.37105},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2610.37105},
}
```
