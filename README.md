# University collaborator discovery

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23529614.svg)](https://doi.org/10.5281/zenodo.23529614)

Code and frozen study inputs for **University collaborator discovery using language models and source-linked publication evidence**, by Chao Chen, Chao Li, Youdong Wang and Haijian Zhu, Network and Information Center, Southeast University.

The workflow turns a faculty research need into candidate collaboration cards with publication evidence and conditional rationales. The study covers two institutional needs and compares BM25, semantic retrieval, and association-based evidence selection. The results are descriptive; they do not establish ranking superiority or subsequent collaboration.

## Quick start: offline reproduction

Python 3.12 is recommended. Clone the repository with its six compressed corpus parts, then run:

```bash
git clone https://github.com/seucchen-eng/university-collaborator-discovery.git
cd university-collaborator-discovery
python -m venv .venv
```

Activate the environment (`.venv\Scripts\activate` on Windows, or `source .venv/bin/activate` on macOS/Linux), then:

```bash
python -m pip install -r requirements-replay.txt
python code/replay.py
```

The replay reads the compressed corpus directly. It makes no network requests, model-inference calls, or paid API calls. It writes `verification/offline_replay.json` and `evaluation/recomputed_results.json`. These files are tracked study reports, so a new execution can change the recorded runtime and timestamp. For the smaller human-result calculation alone, run:

```bash
python evaluation/summarize_open_results.py
```

The repository includes about 82 MB of compressed corpus inputs plus code and study records. No Git LFS or model weights are required for the default replay.

## What is included

| Directory/file | Contents |
| --- | --- |
| `code/` | Acquisition, normalization, parallel encoding, retrieval rules, ranking, generation and offline replay |
| `corpus/` | Six compressed parts of the exact 87,101-record retained OpenAlex corpus |
| `corpus_manifest.json` | Partition order, hashes and the original concatenated corpus hash |
| `frozen/` | Queries, retrieval configuration, complete scores and rankings, evidence graph, screening decisions and saved generation inputs/outputs |
| `evaluation/` | Coded labels, evaluated cards, selected source passages and result aggregation |
| `records/` | Historical acquisition/runtime records and portability notes |
| `model/` | Encoder revision, artifact hashes and upstream model card; no weights |
| `verification/` | Archived and repository replay results |
| `FIELD_DICTIONARY.md` | Field definitions, denominators and interpretation |

All evaluated records were copied from the frozen release package. No new human evaluations or model outputs were generated for publication. Expected core checks include 87,101 corpus records, 174,202 BM25 values, 1,553 ranked author objects, six generation packets, 17 cards and 32 factual statements. Identity review leaves 16 eligible cards representing 14 people; nine card instances representing seven people received definite interest.

## Reproduction boundaries

The offline replay recalculates corpus accounting, lexical scores, rankings and human-result summaries from the archived inputs. Semantic scores and hosted-model responses are frozen inputs; the default command does not regenerate them. Public-source updates and hosted-model changes can make a fresh run differ from the historical study. Candidate identity screening is replayed as a recorded decision, not independently re-established.

The hosted service returned the `deepseek-flash` alias on 26 September 2026 UTC with fingerprint `aeb56401ca74e127821c4f9126dcb669`; an immutable API model version was not returned. The encoder revision is recorded in `model/manifest.json`. Original and replay runtime versions are kept separately.

## Optional new acquisition or model execution

The implementations for a new run are included, but their execution is separate from the frozen replay. `fetch_public_data.py` uses `OPENALEX_API_KEY` and a new `STUDY_WORK_DIR`; its network acquisition is disabled by default. `normalize_corpus.py` prepares a new snapshot. `encoder.py` needs the model files listed in `model/manifest.json`, a separate work directory and `requirements-encoder.txt`.

`generate.py` additionally requires `ALLOW_PAID_REGENERATION=YES` and `DEEPSEEK_API_KEY`. New generation can incur charges and is not run by the reproduction command. Keep credentials in environment variables, never in this repository. Detailed original implementation notes are retained in `records/portable_adaptations.json`.

## Ethics, consent and licenses

The Science and Technology Ethics Committee of Southeast University approved subsequent analysis and publication of existing materials under the submitted protocol (SEU-EC-2026-0059; reviewed 12 October 2026, issued 19 October 2026). The evaluations preceded the decision. The author subsequently confirmed reconfirmation of the materials and original opinions with responsible contributors, without changing the data, and authorization for analysis and open public release of study data, including item-level records.

MIT applies to author-controlled code, documentation and study data as described in `LICENSE`. Third-party publication text, OpenAlex metadata and model assets retain their source terms; see `THIRD_PARTY_NOTICES.md`. Public bibliography and source links can identify candidate authors. Private participant crosswalks, signed forms, approval scans, personal contact records and raw feedback prose are excluded from this repository.

## Citation and contact

Use the repository version or commit you actually used; `CITATION.cff` supplies software citation metadata. The associated manuscript is in preparation for submission and has no publication DOI recorded here. This GitHub repository has no archival DOI yet.

Correspondence: Chao Chen, cchen@seu.edu.cn.
