# Evaluating 8B-Parameter LLMs for English-Russian Translation and Methods to Improve Performance

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Official code for **"Evaluating 8B-Parameter LLMs for English-Russian Translation and Methods to Improve Performance"** by Tikhon Inogamov and Faisal Nawab, published in *Curieux Academic Review* (2026 August Issue, Issue 10 Part 1, pp. 101-114).

[Paper (PDF)](https://www.curieuxreview.com/_files/ugd/60ed3c_f30d24aafaaf400cbf1a70353900f0a2.pdf)

<!-- TODO: add an overview figure from the paper -->
<!-- ![Overview](assets/overview.png) -->

## Summary
This work evaluates how well 8B-parameter large language models translate between English and Russian, and tests methods for improving their performance.

<!-- TODO: add 1-2 sentences: which models were compared, which improvement methods were tried, and the main finding -->

## Citation
```bibtex
@article{inogamov2026evaluating,
  title   = {Evaluating 8B-Parameter LLMs for English-Russian Translation and Methods to Improve Performance},
  author  = {Inogamov, Tikhon and Nawab, Faisal},
  journal = {Curieux Academic Review},
  note    = {August Issue, Issue 10, Part 1},
  pages   = {101--114},
  year    = {2026}
}
```

## Repository Structure
```
├── Embedding_test/      # Text parts, translations and ratings generated during testing embedding model's impact
├── input/               # Input text that will be translated
├── temp_tests/          # Text parts, translations and ratings generated during temperature testing
└── /.                   # Scripts for various parts of experiments, text corpora, and logs
```

## Installation
```bash
git clone https://github.com/MurometzZ/LLM-Translation-Optimization.git
cd LLM-Translation-Optimization
```
Tested with Python 3.14.

Hardware: At least 8GB VRAM recommended (8B models typically need a GPU with enough memory to load the weights).

Note: due to the inherent randomness of LLMs, results may vary slightly. 

## Models and Data
- Models evaluated: LLaMA 3.1 8B, Qwen3 8B, and YandexGPT-5 Lite 8B
- Evaluation dataset(s): Crime and Punishment by Fyodor Dostoevsky, RusLTC article pair (RusLTC_EN_1_94 and RusLTC_RU_1_94_1)
- Metrics: 0 to 10 rating system, with large cloud LLM used to rate translations

## Inner workings
```python
  # Example of how basic temperature testing was executed  
  answers = []
  for _ in range(generations):
      answer = ask_llm(instructions + content, model, temperature)
      answers.append(answer)
  for i, ans in enumerate(answers):
      new_filepath = translations_dir / folder_name / (file.stem + "_translation.txt")
      create_file_with_text(new_filepath.with_name(f"{new_filepath.stem}_{i}{new_filepath.suffix}"), ans)
```

## Acknowledgments
Supervised by Faisal Nawab (mentor)

## License
Code in this repository is released under the [MIT License](LICENSE).
Models and datasets used in the paper are subject to their own licenses.
