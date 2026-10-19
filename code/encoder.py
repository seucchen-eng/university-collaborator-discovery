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

def normalize_doi(d):
    return re.sub('^https?://(dx\\.)?doi.org/', '', d or '', flags=re.I).lower().strip()

def name_norm(s):
    return re.sub('[^a-z]', '', (s or '').lower())

def reconstruct(index):
    if not index:
        return (None, 'missing_abstract')
    toks = {}
    for word, positions in index.items():
        for pos in positions:
            if pos in toks and toks[pos] != word:
                return (None, 'abstract_position_collision')
            toks[pos] = word
    if len(toks) != max(toks) + 1:
        return (None, 'abstract_position_gap')
    return (' '.join((toks[i] for i in range(len(toks)))), None)

def canonical(a, doi, resolutions):
    aid = (a['author'].get('id') or '').split('/')[-1]
    names = {name_norm(a['author'].get('display_name')), name_norm(a.get('raw_author_name'))}
    raw = ' '.join(a.get('raw_affiliation_strings') or [])
    for r in resolutions:
        if 'raw_affiliation_pattern' not in r or aid not in r['ids']:
            continue
        if not names & {name_norm(n) for n in r['names']}:
            continue
        if doi in r['paper_doi_overrides'] or re.search(r['raw_affiliation_pattern'], raw, re.I):
            return r['local_key']
    return aid

def init_encoder():
    global TOKENIZER, SESSION
    from tokenizers import Tokenizer
    import onnxruntime as ort
    TOKENIZER = Tokenizer.from_file(str(MODEL / 'tokenizer.json'))
    TOKENIZER.enable_truncation(max_length=256)
    TOKENIZER.enable_padding(pad_id=0, pad_token='[PAD]')
    options = ort.SessionOptions()
    options.intra_op_num_threads = 4
    options.inter_op_num_threads = 1
    SESSION = ort.InferenceSession(str(MODEL / 'onnx/model_quint8_avx2.onnx'), sess_options=options, providers=['CPUExecutionProvider'])

def encode(texts):
    import numpy as np
    batch = TOKENIZER.encode_batch(texts)
    assert all((not e.overflowing for e in batch)), 'Common visibility failed: encoder still truncates.'
    values = {'input_ids': np.array([e.ids for e in batch], dtype=np.int64), 'attention_mask': np.array([e.attention_mask for e in batch], dtype=np.int64), 'token_type_ids': np.array([e.type_ids for e in batch], dtype=np.int64)}
    result = SESSION.run(None, {i.name: values[i.name] for i in SESSION.get_inputs()})[0]
    mask = values['attention_mask'][..., None]
    pooled = (result * mask).sum(axis=1) / np.clip(mask.sum(axis=1), 1e-09, None)
    pooled /= np.clip(np.linalg.norm(pooled, axis=1, keepdims=True), 1e-09, None)
    return pooled.astype(np.float32)

def encode_chunk(index, texts, input_hash):
    import numpy as np
    dest = BASE / 'embedding_parts' / f'{index:04d}.npy'
    receipt = dest.with_suffix('.json')
    if dest.exists() and receipt.exists():
        r = load(receipt)
        assert r['input_sha256'] == input_hash and sha(dest) == r['output_sha256']
        return r
    started = time.perf_counter()
    values = np.concatenate([encode(texts[start:start + 32]) for start in range(0, len(texts), 32)])
    np.save(dest, values)
    result = {'chunk': index, 'rows': len(texts), 'seconds': time.perf_counter() - started, 'input_sha256': input_hash, 'output_sha256': sha(dest)}
    save(receipt, result)
    return result

def embed():
    import numpy as np
    import onnxruntime as ort
    import tokenizers
    if (BASE / 'embedding_summary.json').exists():
        raise SystemExit('Embedding already complete.')
    assert (BASE / 'corpus.jsonl').exists(), 'Restore the frozen corpus in the work directory first.'
    for f in load(MODEL / 'manifest.json')['files']:
        assert sha(MODEL / f['file']) == f['sha256']
    (BASE / 'embedding_parts').mkdir(exist_ok=True)
    texts = [r['index_text'] for r in rows(BASE / 'corpus.jsonl')]
    started = time.perf_counter()
    chunks = []
    completed = 0
    save(BASE / 'runtime.json', {'python': sys.version, 'platform': platform.platform(), 'cpu_count': os.cpu_count(), 'numpy': np.__version__, 'onnxruntime': ort.__version__, 'tokenizers': tokenizers.__version__, 'workers': 4, 'intra_op_threads_per_worker': 4, 'inter_op_threads': 1, 'batch_size': 32, 'started_utc': now()})
    with ProcessPoolExecutor(max_workers=4, initializer=init_encoder) as pool:
        pending = []
        for start in range(0, len(texts), 1024):
            part = texts[start:start + 1024]
            index = start // 1024
            h = hashlib.sha256(json.dumps(part, ensure_ascii=False).encode()).hexdigest()
            pending.append(pool.submit(encode_chunk, index, part, h))
        for future in as_completed(pending):
            r = future.result()
            chunks.append(r)
            completed += r['rows']
            status = {'completed': completed, 'total': len(texts), 'seconds': time.perf_counter() - started}
            save(BASE / 'embedding_progress.json', status)
            print(json.dumps(status), flush=True)
    vec = np.concatenate([np.load(BASE / 'embedding_parts' / f'{i:04d}.npy') for i in range(len(pending))])
    assert len(vec) == len(texts) and np.isfinite(vec).all()
    np.save(BASE / 'embeddings.npy', vec)
    init_encoder()
    qs = load(BASE / 'queries.json')
    qvec = encode([q['dense_query'] for q in qs])
    np.save(BASE / 'dense_scores.npy', qvec @ vec.T)
    save(BASE / 'embedding_summary.json', {'rows': len(vec), 'shape': list(vec.shape), 'seconds': time.perf_counter() - started, 'revision': load(MODEL / 'manifest.json')['revision'], 'max_norm_error': float(np.max(np.abs(np.linalg.norm(vec, axis=1) - 1))), 'no_additional_encoder_truncation': True, 'completed_utc': now(), 'chunks': sorted(chunks, key=lambda x: x['chunk'])})
    print('Embedding complete.', flush=True)

if __name__=='__main__':
    embed()
