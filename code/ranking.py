"""Portable copy of frozen ranking arithmetic; private requester mapping omitted."""
from pathlib import Path
from collections import defaultdict
import json,gzip
BASE=Path(__file__).resolve().parents[1]/'frozen'
def load(path):return json.loads(Path(path).read_text('utf-8'))
def rows(path):
    path=Path(path)
    if path.name=='corpus.jsonl':
        manifest=load(BASE.parent/'corpus_manifest.json')
        for part in manifest['parts']:
            with gzip.open(BASE.parent/part['file'],'rt',encoding='utf-8') as f:
                for line in f:
                    if line.strip():yield json.loads(line)
    else:
        with path.open(encoding='utf-8') as f:
            for line in f:
                if line.strip():yield json.loads(line)

def rank():
    import numpy as np
    qs = load(BASE / 'queries.json')
    groups = load(BASE / 'author_eligibility.json')
    excluded = load(BASE / 'coauthor_exclusions_verified.json')
    corpus = list(rows(BASE / 'corpus.jsonl'))
    bm = np.load(BASE / 'bm25_scores.npy')
    dense = np.load(BASE / 'dense_scores.npy')
    assert bm.shape == dense.shape == (2, len(corpus)) and np.isfinite(bm).all() and np.isfinite(dense).all()
    traces = []
    queue = defaultdict(lambda: {'occurrences': [], 'papers': {}})
    wanted = set()
    for qi, q in enumerate(qs):
        facets = set(q['facets'])
        for method in ['B1', 'B2', 'G']:
            raw = bm[qi] if method == 'B1' else dense[qi]
            pool = np.argsort(-raw, kind='stable')[:200].tolist()
            wanted.update(pool)
            score = raw / max(float(raw.max()), 1e-09) if method == 'B1' else raw
            byauthor = defaultdict(list)
            for i in pool:
                for key in corpus[i]['seu_authors']:
                    g = groups[key]
                    if g['paper_count'] >= 2 and g['latest_year'] >= 2020 and (key not in excluded[q['query_id']]):
                        byauthor[key].append(i)
            ranked = []
            for key, ids in byauthor.items():
                chosen = []
                covered = set()
                if method == 'G':
                    remaining = list(ids)
                    for _ in range(min(2, len(ids))):
                        i = min(remaining, key=lambda j: (-(0.6 * float(score[j]) + 0.4 * len((set(corpus[j]['facets']) & facets) - covered) / len(facets)), corpus[j]['paper_uid']))
                        chosen.append(i)
                        covered |= set(corpus[i]['facets']) & facets
                        remaining.remove(i)
                    author_score = 0.6 * sum((float(score[i]) for i in chosen)) / len(chosen) + 0.4 * len(covered) / len(facets)
                else:
                    chosen = sorted(ids, key=lambda i: (-float(score[i]), corpus[i]['paper_uid']))[:2]
                    covered = set().union(*(set(corpus[i]['facets']) & facets for i in chosen))
                    author_score = sum((float(score[i]) for i in chosen)) / len(chosen)
                ranked.append({'author_key': key, 'score': author_score, 'facets': sorted(covered), 'papers': [{'uid': corpus[i]['paper_uid'], 'score': float(score[i])} for i in chosen]})
            ranked.sort(key=lambda r: (-r['score'], r['author_key']))
            for pos, r in enumerate(ranked, 1):
                r['rank'] = pos
                if pos <= 12:
                    ent = queue[r['author_key']]
                    ent['occurrences'].append({'query_id': q['query_id'], 'method': method, **r})
                    ent['group'] = groups[r['author_key']]
                    for p in r['papers']:
                        src = next((corpus[i] for i in pool if corpus[i]['paper_uid'] == p['uid']))
                        ent['papers'][p['uid']] = src
            traces.append({'query_id': q['query_id'], 'method': method, 'pool': [corpus[i]['paper_uid'] for i in pool], 'ranked': ranked})
    return traces, dict(queue), wanted
