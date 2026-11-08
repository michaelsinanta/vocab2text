# Text Generation in Low-Resource Languages Using Human-Curated Vocabularies

Code for the paper **[Text Generation in Low-Resource Languages Using Human-Curated Vocabularies](https://arxiv.org/abs/2610.37105v1)**.

![Architecture Diagram](assets/Human_curated_Vocab_page-0001.png)

This repository builds the **prompts** used to ask a large language model to write text in a low-resource language. It does not call any model itself: it writes CSV files of ready-to-use prompts.

## Which prompts to generate

If you want to **replicate the method from the paper**, generate **ours**. Those prompts are the main contribution: few-shot examples plus a list of candidate words from a human-curated dictionary.

**Few-shot** and **zero-shot** are supplementary. They are the baselines we compared against in the paper, not the method to replicate.

| Prompt type                      | Command                                 | What the prompt contains                                                                                     | Role         |
| -------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| [Ours](#ours-paper-method)       | `python -m prompt_generation.ours`      | Task instructions, few-shot examples, and a list of candidate words (POS, English meaning, example sentence) | Paper method |
| [Few-shot](#few-shot-baseline)   | `python -m prompt_generation.few_shot`  | Task instructions + a few human-written example outputs (no dictionary candidates)                           | Baseline     |
| [Zero-shot](#zero-shot-baseline) | `python -m prompt_generation.zero_shot` | A short instruction to write about a topic at a given length (no examples, no dictionary)                    | Baseline     |

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

## Shared settings

All three prompt types read the same lists from `prompt_generation/config.py`:

- **Languages** (`LANGUAGES`): see [Adding a new language](#adding-a-new-language).
- **Length buckets**: `5_words`, `10_words`, `15_words`, `20_words` (one sentence of about that many words) and `paragraph` (at least 3 sentences and at least 25 words).
- **Topics** (`TOPICS`): food, family, holiday, travel, health, fitness, education, technology, music, movies, books, fashion, nature, pets, business, art, science, gaming, home, garden.

---

## Adding a new language

1. The first step is to collect a dictionary. Collect desired dictionary for target language and standardize its entries into a common format. Each entry consists of a target-language word, its English equivalent, an English definition, a part-of-speech (POS) tag, and, when available, an example sentence illustrating its usage.

   Save that dictionary as `dictionaries/<language>.csv`. **Ours** prompt needs these columns:

| Column               | Definition                                                           | Example (in Indonesian)                |
| -------------------- | -------------------------------------------------------------------- | -------------------------------------- |
| `word`               | Target-language word                                                 | `makan`                                |
| `pos_mapped`         | Part of speech                                                       | `verb`                                 |
| `meaning_translated` | English definition of the word                                       | `to put food in the mouth and swallow` |
| `direct_translation` | One-to-one English word translation                                  | `eat`                                  |
| `example`            | Example usage in the target language (optional; leave empty if none) | `Anak-anak makan ubi.`                 |

2. Create the few-shot example files.

   Make a folder `few_shot_prompts/<language>/` and add one file per length you want to generate:

   ```
   few_shot_prompts/<language>/
     5_words.py
     10_words.py
     15_words.py
     20_words.py
     paragraph.py
   ```

   Each file must contain a list named `EXAMPLES`. Each item is one example written by a human:

   ```python
   # few_shot_prompts/<language>/5_words.py
   EXAMPLES = [
       {
           "output": "A sentence written in the language.",
           "word_candidates": "word | pos | meaning | example sentence\n"
                              "word | pos | meaning | example sentence",
       },
       # ... more examples
   ]
   ```

   - `output`: the example text itself. Few-shot and ours both use it.
   - `word_candidates`: the dictionary words that example uses, one per line, in the format `word | pos | meaning | example sentence`.
     You only need files for the lengths you plan to run.

3. Add the display name to `LANGUAGES` in `prompt_generation/config.py`.
4. Run the generator with `--languages <language>`.

---

## Prompt Generation

List what is available:

```bash
python -m prompt_generation.ours --list
python -m prompt_generation.few_shot --list
python -m prompt_generation.zero_shot --list
```

---

### Ours (Paper method)

This is the main method of the paper. Each prompt gives the model task instructions, a few human-written few-shot examples, and a list of candidate words taken from a human-curated dictionary, then asks it to write one sentence or paragraph.

### Requirements

- `dictionaries/<language>.csv`
- `few_shot_prompts/<language>/` with the length files you want to generate

### Run

```bash
python -m prompt_generation.ours \
  --languages minangkabau --lengths 5_words --topics food travel \
  --samples 100 --seed 42
```

### Options

| Option               | Default                                               | Meaning                                                                                   |
| -------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `--languages`        | `minangkabau`                                         | Languages to generate for                                                                 |
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

### Few-shot baseline

A baseline from the paper. Each prompt gives the model task instructions and a few human-written example outputs, then asks for one sentence or paragraph.

### Requirements

- `few_shot_prompts/<language>/` with the length files you want to generate

### Run

```bash
python -m prompt_generation.few_shot \
  --languages minangkabau --lengths 5_words --samples 100 --seed 42
```

### Options

| Option          | Default              | Meaning                                                                             |
| --------------- | -------------------- | ----------------------------------------------------------------------------------- |
| `--languages`   | `minangkabau`        | Languages to generate for                                                           |
| `--lengths`     | `5_words`            | Target output length(s): `5_words`, `10_words`, `15_words`, `20_words`, `paragraph` |
| `--samples`     | 100                  | Prompts per language and length                                                     |
| `--n-few-shot`  | 3                    | Few-shot examples per prompt                                                        |
| `--seed`        | none                 | Base seed; sample _i_ uses `seed + i` for reproducibility                           |
| `--split-by`    | `language`           | Output split: `none`, `language`, `language-length`                                 |
| `--output-dir`  | `./outputs/few_shot` | Where CSVs are written                                                              |
| `--output-name` | `few_shot_prompts`   | Base file name; only used with `--split-by none`                                    |
| `--list`        | off                  | List available languages and length buckets, then exit                              |

### Output

Files are named `<language>_few_shot.csv` (`--split-by language`), `<language>_<length>_few_shot.csv` (`language-length`), or `<output-name>.csv` (`none`).

Each row is one prompt, with these columns: `prompt_id`, `language`, `prompt`, `prompt_type` (`few_shots_only`), `length_category`, `unit`, `target_length_desc`, `target_sentence_length`, `few_shot_sentence_length`, and `n_few_shot`.

---

## Zero-shot baseline

A baseline from the paper. Each prompt is a single short instruction that names the language, length, and a topic. It has **no few-shot examples and no dictionary**.

### Run

```bash
python -m prompt_generation.zero_shot \
  --languages minangkabau --lengths 5_words --topics food travel --samples 100
```

### Options

| Option          | Default               | Meaning                                                                             |
| --------------- | --------------------- | ----------------------------------------------------------------------------------- |
| `--languages`   | `minangkabau`         | Languages to generate for                                                           |
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
