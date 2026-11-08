# Experiments Result & Analysis

This directory contains the experimental notebooks and results for our paper:

**[Text Generation in Low-Resource Languages Using Human-Curated Vocabularies](https://arxiv.org/abs/2610.37105v1)**

## Getting Started

### 1. Install Dependencies

From the repository root, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Authenticate with Hugging Face

Log in to your Hugging Face account to access the experiment results dataset:

```bash
hf auth login
```

Follow the instructions to authenticate using your Hugging Face access token.

### 3. Download Experiment Results

Download all experiment artifacts, including the complete set of 54,000 generated outputs from our Hugging Face dataset repository:

```bash
hf download SEACrowd-CoRaL/experiment_result \
    --repo-type dataset \
    --local-dir experiments
```

This downloads the experiment results into the `experiments/` directory.

## Running the Experiments

After downloading the necessary files:

1. Navigate to the `experiments/` directory.
2. Open the Jupyter notebooks.
3. Run all cells in each notebook to reproduce the corresponding experimental analyses.

The notebooks contain the code used to process the generated outputs, calculate evaluation metrics, aggregate results, and perform the analyses reported in the paper.

## Results

The [`results/`](results/) directory contains the tables and aggregated results reported in the paper.

These files provide a convenient way to inspect the experimental findings without having to execute the notebooks.

They cover the main evaluation dimensions:

- **Fluency:** Human evaluation of generated text quality.
- **Off-Target Rate:** Proportion of generated words that do not appear in the target-language dictionary.
- **Lexical Diversity:** Diversity of valid target-language n-grams.
- **Additional Analyses:**
  - **Inter-Annotator Agreement:** Pearson and Spearman correlations between the two human annotators' fluency ratings, reported by language.
  - **LLM-as-a-Judge Reliability:** Analysis of the reliability of LLM-based fluency evaluation compared with human annotations.
  - **Robustness Under Increasing Generation Volume:** Stress-test experiments evaluating generation quality at increasing output volumes for Hitu and Minangkabau.
  - **Comparative Analysis:** Detailed comparisons across models, thinking modes, prompting strategies, text lengths, and languages.

Refer to the results directory for the corresponding tables and numerical findings presented in the paper.

## Experimental Coverage

The experiments cover the following configurations:

| Dimension            | Configurations                                                |
| -------------------- | ------------------------------------------------------------- |
| Languages            | Indonesian, Vietnamese, Javanese, Minangkabau, Acehnese, Hitu |
| Models               | Gemini 3.5 Flash, Claude Haiku 4.5, GPT-5.4 Mini              |
| Thinking Modes       | Enabled, disabled                                             |
| Prompting Strategies | Zero-shot, few-shot, few-shot with word candidates (**Ours**) |
| Text Lengths         | 5, 10, 15, 20 words, and paragraphs                           |

In total, the main experimental setup consists of **540 configurations**, with 100 generated outputs per configuration, resulting in **54,000 generated outputs**.

## Related Resources

- **Paper:** [Text Generation in Low-Resource Languages Using Human-Curated Vocabularies](https://arxiv.org/abs/2610.37105v1)
- **Experiment Results Dataset:** [SEACrowd-CoRaL/experiment_result](https://huggingface.co/datasets/SEACrowd-CoRaL/experiment_result)

## Citation

If you use this repository or its experimental results, please cite our paper:

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
