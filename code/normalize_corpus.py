"""Archived open-run encoder functions with portable directory configuration.
Run only deliberately; the default replay uses frozen similarities.
"""
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor,as_completed
from datetime import datetime,timezone
import hashlib,json,os,sys,time,re,argparse
PACKAGE=Path(__file__).resolve().parents[1]
BASE=Path(os.environ.get('STUDY_WORK_DIR',str(PACKAGE/'work')))
MODEL=Path(os.environ.get('STUDY_MODEL_DIR',str(PACKAGE/'model')))
TOKENIZER=None
SESSION=None
def now():return datetime.now(timezone.utc).isoformat()
def load(path):return json.loads(Path(path).read_text('utf-8'))
def save(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n','utf-8')
def rows(path):
    with Path(path).open(encoding='utf-8') as f:
        for line in f:
            if line.strip():yield json.loads(line)
def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''):h.update(block)
    return h.hexdigest()

from collections import Counter,defaultdict
import gzip,math
from encoder import normalize_doi,name_norm,reconstruct,canonical
import retrieval_rules
def rules():return retrieval_rules
def write_rows(path,records):
    with Path(path).open('w',encoding='utf-8') as f:
        for row in records:f.write(json.dumps(row,ensure_ascii=False)+'\n')

def prepare():
    if (BASE / 'corpus_freeze.json').exists():
        raise SystemExit('Corpus already frozen; use a separate version for changes.')
    started = time.perf_counter()
    fetched = load(BASE / 'corpus_fetch_summary.json')
    assert len(fetched) == 16 and all((x['downloaded'] == x['expected_at_start'] for x in fetched))
    rule = rules()
    queries = load(PACKAGE / 'frozen/queries.json')
    save(BASE / 'queries.json', queries)
    cfg = load(PACKAGE / 'frozen/retrieval_config.json')
    cfg.update(corpus_years=[2010, 2025], text_definition='title + newline + OpenAlex abstract', common_visibility='leading 254 content WordPieces', facet_text='same visible span', encoder_workers=4, encoder_batch_size=32, onnx_threads_per_worker=4, chunk_size=1024)
    save(BASE / 'retrieval_config.json', cfg)
    from tokenizers import Tokenizer
    tok = Tokenizer.from_file(str(MODEL / 'tokenizer.json'))
    tok.no_padding()
    tok.no_truncation()
    resolutions = load(PACKAGE / 'frozen/author_resolution_rules.json')
    by_id = {}
    excluded = Counter()
    duplicate_log = []
    for path in sorted((BASE / 'raw/corpus').glob('*.json.gz')):
        with gzip.open(path, 'rt', encoding='utf-8') as handle:
            obj = json.load(handle)
        for w in obj['results']:
            if w['id'] in by_id:
                duplicate_log.append({'id': w['id'], 'reason': 'duplicate_work_id', 'raw_page': path.name})
                continue
            by_id[w['id']] = w
    by_doi = {}
    retained = []
    for w in sorted(by_id.values(), key=lambda x: x['id']):
        text, err = reconstruct(w.get('abstract_inverted_index'))
        if err:
            excluded[err] += 1
            continue
        if not w.get('title'):
            excluded['missing_title'] += 1
            continue
        if w.get('is_retracted'):
            excluded['retracted'] += 1
            continue
        doi = normalize_doi(w.get('doi'))
        if doi and doi in by_doi:
            old = by_doi[doi]
            if len(text) > len(old[1]):
                duplicate_log.append({'id': old[0]['id'], 'doi': doi, 'reason': 'duplicate_doi_less_complete'})
                by_doi[doi] = (w, text)
            else:
                duplicate_log.append({'id': w['id'], 'doi': doi, 'reason': 'duplicate_doi_less_complete_or_higher_id'})
            continue
        if doi:
            by_doi[doi] = (w, text)
        else:
            retained.append((w, text))
    retained.extend(by_doi.values())
    retained.sort(key=lambda x: x[0]['id'])
    del by_id, by_doi
    groups = defaultdict(lambda: {'paper_count': 0, 'latest_year': 0, 'names': Counter(), 'raw_names': Counter(), 'affiliations': Counter(), 'source_author_ids': Counter()})
    coauthors = {'T01': {}, 'T02': {}}
    requester_matches = []
    corpus = []
    truncated = 0
    for w, abstract in retained:
        doi = normalize_doi(w.get('doi'))
        mapped = {}
        for a in w.get('authorships', []):
            if not any((i['id'] == 'https://openalex.org/I76569877' for i in a.get('institutions', []))):
                continue
            key = canonical(a, doi, resolutions)
            if not key:
                continue
            mapped[key] = {'display_name': a['author']['display_name'], 'raw_name': a.get('raw_author_name'), 'openalex_author_id': a['author'].get('id'), 'orcid': a['author'].get('orcid'), 'raw_orcid': a.get('raw_orcid'), 'observed_orcids': a['author'].get('observed_orcids', []), 'raw_affiliations': a.get('raw_affiliation_strings') or []}
        if not mapped:
            excluded['no_resolved_SEU_author_id'] += 1
            continue
        source = w['title'] + '\n' + abstract
        e = tok.encode(source, add_special_tokens=False)
        if not e.ids:
            excluded['empty_tokenization'] += 1
            continue
        end = e.offsets[min(254, len(e.ids)) - 1][1]
        visible = source[:end]
        while len(tok.encode(visible, add_special_tokens=False).ids) > 254:
            visible = visible[:-1]
        assert len(tok.encode(visible).ids) <= 256
        truncated += len(e.ids) > 254
        r = {'paper_uid': w['id'].split('/')[-1], 'openalex_id': w['id'], 'doi': doi, 'title': w['title'], 'abstract': abstract, 'year': w['publication_year'], 'publication_date': w['publication_date'], 'type': w['type'], 'language': w.get('language'), 'source_text': source, 'index_text': visible, 'full_wordpieces': len(e.ids), 'visible_chars': len(visible), 'source_text_sha256': hashlib.sha256(source.encode()).hexdigest(), 'index_text_sha256': hashlib.sha256(visible.encode()).hexdigest(), 'seu_authors': mapped, 'facets': sorted((k for k, rx in rule.RX.items() if rx.search(visible))), 'open_access': w.get('open_access'), 'primary_location': w.get('primary_location'), 'updated_date': w.get('updated_date'), 'metadata_license': 'CC0'}
        corpus.append(r)
        for key, a in mapped.items():
            g = groups[key]
            g['paper_count'] += 1
            g['latest_year'] = max(g['latest_year'], r['year'])
            g['names'][a['display_name']] += 1
            g['raw_names'][a['raw_name'] or ''] += 1
            g['affiliations'].update(a['raw_affiliations'])
            g['source_author_ids'][a['openalex_author_id']] += 1
    del retained
    write_rows(BASE / 'corpus.jsonl', corpus)
    save(BASE / 'author_groups.json', dict(groups))
    save(BASE / 'duplicate_exclusions.json', duplicate_log)
    summary = {'downloaded_records': sum((x['downloaded'] for x in fetched)), 'eligible_papers': len(corpus), 'exclusions': dict(excluded), 'duplicates': len(duplicate_log), 'author_groups': len(groups), 'eligible_author_groups': sum((a['paper_count'] >= 2 and a['latest_year'] >= 2020 for a in groups.values())), 'truncated_records': truncated, 'query_coauthor_excluded_groups': {q: len(v) for q, v in coauthors.items()}, 'seconds': time.perf_counter() - started, 'corpus_sha256': sha(BASE / 'corpus.jsonl')}
    save(BASE / 'scan_summary.json', summary)
    terms = set((t for q in queries for t in rule.tokens(q['search_text'])))
    df = Counter()
    stats = []
    lengths = []
    for r in corpus:
        c = Counter(rule.tokens(r['index_text']))
        short = {t: c[t] for t in c.keys() & terms}
        stats.append(short)
        df.update(short)
        lengths.append(sum(c.values()))
    df = Counter((t for c in stats for t in c))
    import numpy as np
    scores = np.zeros((len(queries), len(corpus)), dtype=np.float32)
    avgdl = sum(lengths) / len(lengths)
    n = len(corpus)
    for qi, q in enumerate(queries):
        queryterms = set(rule.tokens(q['search_text']))
        for i, count in enumerate(stats):
            for t in sorted(queryterms & count.keys()):
                tf = count[t]
                scores[qi, i] += math.log(1 + (n - df[t] + 0.5) / (df[t] + 0.5)) * tf * 2.5 / (tf + 1.5 * (0.25 + 0.75 * lengths[i] / avgdl))
    np.save(BASE / 'bm25_scores.npy', scores)
    save(BASE/'normalization_receipt.json', summary)
    print(json.dumps(summary), flush=True)

if __name__=='__main__':
    prepare()
