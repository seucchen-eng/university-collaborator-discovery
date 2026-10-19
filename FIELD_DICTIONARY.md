# Field dictionary and analysis rules

The evaluated card text remains in Chinese. English explanations below describe the fields; they do not replace what participants read. Public candidate names in operational metadata are distinct from coded participant identities, which are withheld.

## Corpus and retrieval

- `paper_uid`: stable short OpenAlex work identifier (`W...`); `openalex_id`: full URL; `doi`: normalized DOI.
- `title`, `abstract`, `source_text`: title, reconstructed abstract, and the exact title/newline/abstract text. Original retained bibliographic rows are preserved without editing.
- `index_text`: leading source span with at most 254 content WordPieces, common to all three retrieval configurations and signal matching.
- `source_text_sha256`, `index_text_sha256`: SHA-256 of UTF-8 text, without an added newline.
- `full_wordpieces`, `visible_chars`: untruncated content-token count and retained character length. Values over 254 indicate truncation.
- `seu_authors`: institutional author-key dictionary. Author keys are provisional OpenAlex identifiers or bounded local resolutions; raw names, affiliations and observed ORCIDs are public metadata, not confirmed whole-person profiles.
- `facets`: sorted regex-matched research signals. Presence is lexical evidence, not semantic relevance or a transfer relation.
- `primary_location`, `open_access`, `metadata_license`: provider provenance. `metadata_license=CC0` records the provider dataset description, not a new license granted by the study authors over underlying articles.
- `bm25_scores.npy`, `dense_scores.npy`: little-endian NumPy float32 matrices, shape `(2, 87101)`. Row order is `queries.json` (T01 then T02); columns follow the original corpus order. No labels enter their computation.
- `author_eligibility.json`: exact per-group corpus paper count and latest publication year. At least two institutional papers and one from 2020 onward were required.
- `coauthor_exclusions_verified.json`: coded per-query excluded author keys with supporting work IDs. This is the final reviewed exclusion set (T01: 0; T02: 40), not the initial 55-group set. Requester identity crosswalks are omitted.
- `retrieval_trace.json`: six query/configuration objects. `pool` gives the top 200 paper IDs. `ranked` contains every eligible author's `score`, stable `rank`, matched facets and up to two papers with scores.

## Screening, generation and graph

- `identity_decisions.json`: recorded operational desktop screening, marked `independent_human_label=false`. `verified_for_this_run` is bounded to the supplied candidate/profile/paper correspondence; `unresolved` is not a negative faculty judgment. `not_reviewed_beyond_stop` denotes no review.
- `selected_candidates.json`: the exact reviewed prefix and selections before generation. `checked_until_stop` records duplicates and missing selected-paper confirmation.
- `inference_inputs.jsonl`: six packets containing a technical need, fixed candidate order and title/abstract passages capped at 5,500 characters per paper.
- `request_*.json`, `response_*.json`: exact saved HTTP JSON bodies, without authorization headers. `api_ledger.jsonl` contains request hashes, timestamps, costs and returned model/fingerprint/usage fields.
- `outputs.jsonl`: parsed saved model content. Each fact has `statement` (Chinese claim), `quote` (original contiguous English quotation) and `paper_uid`. `rationale` gives a conditional collaboration proposal; `unknowns` lists conditions requiring confirmation. These are hypotheses, not realized collaborations.
- `retrieved_graph.json`: paper/author/signal/need nodes and provenance edges. `MENTIONS` offsets refer to `index_text`; `COAUTHORED` retains original institutional authorship metadata. It does not encode personal contribution or method-transfer truth.

## Coded human data

- `card_id`: frozen K001–K017 identifier; `person_code`: P001–P015, consistent across repeated cards. `query`: T01 or T02. `method`: B1 (BM25), B2 (MiniLM), or G (association selection).
- `fact_labels.json`: one row for F001–F032. `V-M` and `V-E` are the two domain reviewers' original ratings; `final_label` is the retained final result. `initial_agreement` must be computed before consensus. F028 originally differed (F2/F1) and later received joint F2.
- F2: fully supported in the supplied quotation/context. F1: partly supported. F0: unsupported or contradicted. FU: unable to judge.
- `card_ratings.json` / `reason_label`: R2 reasonable conditional proposal; R1 local revision required; R0 untenable; RU unable to judge. Each rationale has one domain review, assigned by specialty.
- `personal_attribution_flag`: wording overstates what publication coauthorship establishes about the individual's contribution. It is a separate flag and does not automatically change the R label.
- `interest`: `yes` = definite interest in further investigation; `conditional` = consider after more information; `no` = not worth following up; `unknown` = unable to judge.
- `entry`: `yes` = concrete collaboration entry point; `no` = no concrete entry point; `unknown` = uncertain. No eligible negative responses occurred.
- `identity_eligible`, `analysis_included`: primary utility inclusion. Both false for K004/P010. This identity exclusion does not remove that card from actual exposure or source/rationale checks.
- `frozen_card_content.json`: coded original statements, quotes, `rationale_zh` and `conditions_zh`. No raw participant commentary is copied.

## Denominators

All generated content: 17 cards / 15 people / 32 facts / 30 papers. Initial factual agreement: 31/32. Final factual support: 32 F2. Rationales: 12 R2 and 5 R1. Primary requester analysis: 16 cards / 14 people, with 9 definite-interest and 7 conditional-interest cards. The 9 definite-interest instances concern 7 distinct people. Concrete entry points: 11 yes and 5 uncertain. Configuration/case counts are descriptive; cards are not independent trials.
