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

import urllib.request,urllib.error
from fetch_public_data import NoRedirect
def raise_unless_explicit():
    if os.environ.get('ALLOW_PAID_REGENERATION')!='YES':
        raise SystemExit('Paid regeneration disabled. Frozen output replay requires no API.')
    if BASE.resolve()==(PACKAGE/'frozen').resolve():
        raise SystemExit('Never overwrite the frozen run. Use a new work directory.')

def append(path, obj):
    with path.open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(obj, ensure_ascii=False) + '\n')

def cost(inp, out, cfg):
    return (inp * cfg['peak_input_cny_per_million'] + out * cfg['peak_output_cny_per_million']) / 1000000.0

def run():
    raise_unless_explicit()
    cfg = load(BASE / 'generation_config.json')
    assert cfg['endpoint'] == 'https://api.deepseek.com/chat/completions' and cfg['model'] == 'deepseek-flash'
    key = os.environ.get('DEEPSEEK_API_KEY')
    if not key:
        raise SystemExit('DEEPSEEK_API_KEY absent; no value printed.')
    inputs = {(r['query_id'], r['method']): r['packet'] for r in rows(BASE / 'inference_inputs.jsonl')}
    events = list(rows(BASE / 'api_ledger.jsonl')) if (BASE / 'api_ledger.jsonl').exists() else []
    starts = {e['request_id']: e for e in events if e['event'] == 'reserved'}
    ends = {e['request_id']: e for e in events if e['event'] == 'finished'}
    assert not starts.keys() - ends.keys(), 'Unresolved paid attempt; do not duplicate.'
    assert all((e['status'] == 'ok' for e in ends.values())), 'Prior failure; inspect before any further calls.'
    spent = sum((e['charged_upper_cny'] for e in ends.values()))
    done = {(e['query_id'], e['method']) for e in ends.values()}
    opener = urllib.request.build_opener(NoRedirect())
    for q, m in [('T01', 'B1'), ('T01', 'B2'), ('T01', 'G'), ('T02', 'G'), ('T02', 'B2'), ('T02', 'B1')]:
        if (q, m) in done:
            continue
        payload = {k: cfg[k] for k in ['model', 'temperature', 'thinking', 'reasoning_effort', 'max_tokens', 'response_format']}
        payload['messages'] = [{'role': 'system', 'content': (BASE / 'prompt.txt').read_text('utf-8')}, {'role': 'user', 'content': json.dumps(inputs[q, m], ensure_ascii=False)}]
        body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        reserve = cost(len(body) + 1024, cfg['max_tokens'], cfg)
        if spent + reserve > cfg['study_budget_cny']:
            raise SystemExit('Budget reached.')
        rid = f'{q}-{m}-{time.time_ns()}'
        path = BASE / ('request_' + rid + '.json')
        path.write_bytes(body)
        append(BASE / 'api_ledger.jsonl', {'event': 'reserved', 'request_id': rid, 'query_id': q, 'method': m, 'utc': now(), 'reserved_cny': reserve, 'request_sha256': sha(path)})
        started = time.perf_counter()
        charge = reserve
        status = 'failed'
        error = None
        meta = {}
        try:
            req = urllib.request.Request(cfg['endpoint'], data=body, headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'}, method='POST')
            with opener.open(req, timeout=60) as response:
                raw_bytes = response.read()
            (BASE / ('response_' + rid + '.json')).write_bytes(raw_bytes)
            raw = json.loads(raw_bytes)
            meta = {k: raw.get(k) for k in ['id', 'created', 'model', 'usage', 'system_fingerprint']}
            usage = raw.get('usage', {})
            if all((type(usage.get(k)) is int for k in ['prompt_tokens', 'completion_tokens'])):
                charge = cost(usage['prompt_tokens'], usage['completion_tokens'], cfg)
            status = 'invalid_output'
            choice = raw['choices'][0]
            assert choice['finish_reason'] == 'stop', 'non_stop_finish'
            obj = json.loads(choice['message']['content'])
            assert obj['query_id'] == q and isinstance(obj['candidates'], list), 'schema_error'
            append(BASE / 'outputs.jsonl', {'query_id': q, 'method': m, 'request_id': rid, 'output': obj})
            status = 'ok'
        except urllib.error.HTTPError as exc:
            error = 'HTTP_' + str(exc.code)
        except urllib.error.URLError as exc:
            error = 'network_' + type(exc.reason).__name__
        except Exception as exc:
            error = type(exc).__name__ + ':' + str(exc)[:100]
        spent += charge
        append(BASE / 'api_ledger.jsonl', {'event': 'finished', 'request_id': rid, 'query_id': q, 'method': m, 'utc': now(), 'status': status, 'error': error, 'charged_upper_cny': charge, 'latency_seconds': time.perf_counter() - started, **meta})
        print(json.dumps({'query': q, 'method': m, 'status': status, 'error': error, 'cost_upper': spent}), flush=True)
        if status != 'ok':
            raise SystemExit('Stopped; original attempt retained.')

if __name__=='__main__':
    run()
