# University collaborator discovery using language models and source-linked publication evidence — code and data package

## Title

Open institutional collaborator-discovery experiment: portable code, frozen study records and normalized OpenAlex corpus for the two reported cases.

## Description

This package accompanies the manuscript *University collaborator discovery using language models and source-linked publication evidence* (Chao Chen, Chao Li, Youdong Wang, Haijian Zhu). It provides the exact inputs and outputs of the reported run: a normalized institutional OpenAlex corpus (87,101 records, 2010–2025), frozen lexical and semantic scores, six complete rankings, operational identity decisions, selected source evidence, exact generated suggestion cards, and coded human evaluation labels. The package reproduces the archived outputs from frozen inputs; it does not create new recommendations or new participant data.

Institutional approval: SEU-EC-2026-0059 (reviewed 12 October 2026, issued 19 October 2026). The reported human evaluation was conducted on 20–23 October 2026 with written informed consent. Named participant forms and identity crosswalks are excluded.

## Dataset Information

- `PREPARATION/corpus/part_01.jsonl.gz` … `part_06.jsonl.gz` (external, in the Zenodo deposit and GitHub repository): six ordered, byte-preserving partitions of the normalized corpus. Concatenate decompressed parts in manifest order to restore `corpus.jsonl` (SHA-256: `a4fe2ecb27529d548026ae7465075ebbe68fd60183705de03a4c7aee8894b781`).
- `PREPARATION/corpus_manifest.json`: partition hashes, record counts and original corpus SHA-256.
- `PREPARATION/frozen/`: queries, retrieval settings, BM25 and dense scores, full rankings, exclusion set, identity decisions, generation inputs, prompts, HTTP request/response bodies and evidence graph.
- `PREPARATION/evaluation/`: coded fact/rationale/requester labels, frozen Chinese card content, selected source texts and summary script.
- `PREPARATION/records/`: freeze manifests, accounting records, runtime and hardware records, encoder receipts and adaptation log.
- `PREPARATION/model/`: pinned third-party model manifest and model card (weights are not bundled).

**Language note:** the evaluated suggestion cards, prompts and source passages contain Chinese text because the instruments were administered in Chinese. English reading translations of the cards, instructions and scoring rules are provided in `Supplemental_Methods_S1.zip` (`card_reading_companion_en.md`, `EN_operations_and_scoring.md`, and the `en/` instrument translations). These translations are reading aids, not new evaluations.

## Code Information

- `PREPARATION/code/replay.py`: offline verification of corpus bytes, source hashes, BM25 values, rankings, identity gate, generation packets and human-result tables. No network or paid API calls.
- `PREPARATION/code/ranking.py`: frozen ranking arithmetic.
- `PREPARATION/code/retrieval_rules.py`: retrieval and selection rules.
- `PREPARATION/code/normalize_corpus.py`: corpus normalization (deduplication, abstract reconstruction, institutional-author mapping, 254-WordPiece retrieval span and BM25).
- `PREPARATION/code/encoder.py`: parallel embedding encoder (requires separately downloaded model weights).
- `PREPARATION/code/fetch_public_data.py`: gated OpenAlex acquisition for a fresh snapshot.
- `PREPARATION/code/generate.py`: gated paid regeneration; not invoked by replay.
- `PREPARATION/evaluation/summarize_open_results.py`: recalculation of evaluation summaries.

All code comments and documentation are in English. Chinese strings that remain inside code or data are evaluated source content, not comments.

## Usage Instructions

1. Extract `Supplemental_Code_S1.zip` to obtain `PREPARATION/`.
2. Download the six corpus partitions from Zenodo (DOI below) or GitHub and copy them into `PREPARATION/corpus/`.
3. Verify files against `PREPARATION/FILE_MANIFEST.json` (byte sizes and SHA-256).
4. Run the offline replay:

   ```text
   python PREPARATION/code/replay.py
   ```

   Results are written to `PREPARATION/verification/offline_replay.json` and `PREPARATION/evaluation/recomputed_results.json`.

Do not overwrite the original labels after reading the summary.

### Optional full-pipeline implementation

If you want to run the pipeline rather than replay the archived outputs:

1. Acquire raw OpenAlex records with `PREPARATION/code/fetch_public_data.py` (requires `OPENALEX_API_KEY` and a fresh `STUDY_WORK_DIR`; disabled by default).
2. Normalize them with `PREPARATION/code/normalize_corpus.py` to produce `corpus.jsonl` and the shared 254-WordPiece retrieval text.
3. Download the model weights listed in `PREPARATION/model/manifest.json` and run `PREPARATION/code/encoder.py` (set `STUDY_MODEL_DIR` and `STUDY_WORK_DIR`).
4. Compute the six rankings with `PREPARATION/code/ranking.py` and `PREPARATION/code/retrieval_rules.py`.
5. Generate new cards only with `PREPARATION/code/generate.py` (requires `ALLOW_PAID_REGENERATION=YES` and `DEEPSEEK_API_KEY`). Regeneration is a new run and is outside the validation reported in the manuscript.

## Requirements

- Python 3.12 (the saved replay used Python 3.12.14).
- NumPy 2.4.4 for replay (`PREPARATION/requirements-replay.txt`).
- Original encoder dependencies are preserved in `PREPARATION/requirements-encoder.txt` (NumPy 2.5.3, onnxruntime 1.30.0, tokenizers 0.23.2).
- No packages are installed automatically by the scripts.

## Methodology

The workflow selects candidate researchers from an institutional OpenAlex corpus under a fixed evidence budget, then generates suggestion cards whose factual statements carry exact bounded quotations. Candidate identities and order are frozen before card generation. Human evaluation separates identity eligibility, factual support, rationale quality and requester interest with explicit denominators. The offline replay verifies the saved outputs without repeating human judgments or calling the hosted generator.

## Citations

Manuscript: *University collaborator discovery using language models and source-linked publication evidence*, Chao Chen, Chao Li, Youdong Wang and Haijian Zhu. Correspondence: cchen@seu.edu.cn.

Archive DOI: https://doi.org/10.5281/zenodo.23972385
Source repository: https://github.com/seucchen-eng/university-collaborator-discovery

## License & Contribution Guidelines

Author-controlled code, documentation and study data are released under the MIT License (see `PREPARATION/LICENSE` and `PREPARATION/THIRD_PARTY_NOTICES.md`). OpenAlex describes its released dataset as CC0; third-party publication text and model assets retain their original terms. No publisher full-text PDF is included.

If you use this package, please cite the manuscript and the archive DOI. Issues and pull requests may be opened on GitHub; changes that would alter frozen cards, original ratings or labels should be proposed as new analysis branches, not as edits to the frozen records.
