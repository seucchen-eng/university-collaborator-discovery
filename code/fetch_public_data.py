"""Frozen public metadata acquisition for the open-data collaborator-discovery run."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import argparse
import gzip
import hashlib
import json
import os
import ssl
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
BASE=Path(os.environ.get('STUDY_WORK_DIR',str(Path(__file__).resolve().parents[1]/'work')))
LOCK = threading.Lock()

def now():
    return datetime.now(timezone.utc).isoformat()

def load(path):
    return json.loads(Path(path).read_text('utf-8'))

def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', 'utf-8')
    temp.replace(path)

class NoRedirect(urllib.request.HTTPRedirectHandler):

    def redirect_request(self, req, fp, code, msg, hdrs, newurl):
        return None

def fetch(name, url, allow_missing=False):
    dest = BASE / 'raw' / f'{name}.json.gz'
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        with gzip.open(dest, 'rt', encoding='utf-8') as handle:
            return json.load(handle)
    host = urllib.parse.urlsplit(url).hostname
    if host not in {'api.openalex.org', 'api.crossref.org', 'api.openaire.eu'}:
        raise ValueError('Unexpected API host')
    headers = {'User-Agent': 'SEU-open-collaborator-discovery/1.0', 'Accept': 'application/json'}
    if host == 'api.openalex.org':
        key = os.environ.get('OPENALEX_API_KEY')
        if not key:
            raise RuntimeError('OPENALEX_API_KEY missing; no value printed.')
        headers['Authorization'] = 'Bearer ' + key
    opener = urllib.request.build_opener(NoRedirect())
    for attempt in range(3):
        started = now()
        try:
            with opener.open(urllib.request.Request(url, headers=headers), timeout=45) as response:
                raw = response.read()
                rate = {k: v for k, v in response.headers.items() if k.lower().startswith('x-ratelimit')}
            obj = json.loads(raw)
            temp = dest.with_suffix('.tmp')
            with gzip.open(temp, 'wb', compresslevel=4) as handle:
                handle.write(raw)
            temp.replace(dest)
            with LOCK:
                with (BASE / 'fetch_ledger.jsonl').open('a', encoding='utf-8') as handle:
                    handle.write(json.dumps({'name': name, 'url': url, 'utc': started, 'attempt': attempt + 1, 'sha256_raw': hashlib.sha256(raw).hexdigest(), 'rate': rate}) + '\n')
            time.sleep(0.1)
            return obj
        except urllib.error.HTTPError as exc:
            if exc.code == 400:
                detail = exc.read().decode('utf-8', 'replace')[:1500]
                print(json.dumps({'request': name, 'http': 400, 'detail': detail}), flush=True)
            if allow_missing and exc.code in (404, 410):
                return {'lookup_status': 'not_found', 'http_status': exc.code}
            if exc.code in (500, 502, 503, 504) and attempt < 2:
                time.sleep(2 * (attempt + 1))
                continue
            raise RuntimeError(f'{name}: HTTP {exc.code}') from None
        except urllib.error.URLError as exc:
            if isinstance(exc.reason, (TimeoutError, ssl.SSLEOFError, ConnectionResetError)) and attempt < 2:
                with LOCK:
                    print(json.dumps({'request': name, 'attempt': attempt + 1, 'retry': type(exc.reason).__name__}), flush=True)
                time.sleep(2 * (attempt + 1))
                continue
            raise RuntimeError(f'{name}: network {type(exc.reason).__name__}') from None
        except TimeoutError:
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
                continue
            raise RuntimeError(f'{name}: timeout after three attempts') from None
    raise RuntimeError('Unexpected retry state')

def url(base, params):
    return base + '?' + urllib.parse.urlencode(params)
FIELDS = 'id,doi,title,publication_year,publication_date,type,language,abstract_inverted_index,authorships,open_access,primary_location,updated_date,is_retracted'

def corpus_year(year):
    cursor = '*'
    page = 1
    found = 0
    expected = None
    started = time.monotonic()
    while cursor:
        if page > 250 or time.monotonic() - started > 5400:
            raise RuntimeError(f'Year {year}: bounded fetch limit reached.')
        params = {'filter': f'authorships.institutions.id:I76569877,publication_year:{year},type:article|review|conference-paper,has_abstract:true', 'per_page': 100, 'cursor': cursor, 'select': FIELDS, 'sort': 'publication_date:asc', 'corpus': 'core'}
        obj = fetch(f'corpus/{year}_{page:04d}', url('https://api.openalex.org/works', params))
        if expected is None:
            expected = obj['meta']['count']
        records = obj.get('results', [])
        found += len(records)
        next_cursor = obj['meta'].get('next_cursor')
        if not records:
            break
        if page % 10 == 0:
            print(json.dumps({'year': year, 'pages': page, 'records': found, 'expected_at_start': expected}), flush=True)
        if next_cursor == cursor:
            raise RuntimeError('Cursor did not advance.')
        cursor = next_cursor
        page += 1
    status = {'year': year, 'expected_at_start': expected, 'downloaded': found, 'pages': page, 'seconds': time.monotonic() - started, 'utc': now()}
    save(BASE / f'corpus_fetch_{year}.json', status)
    print(json.dumps(status), flush=True)
    return status

def corpus():
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(corpus_year, year) for year in range(2010, 2026)]
        results = [f.result() for f in as_completed(futures)]
    save(BASE / 'corpus_fetch_summary.json', sorted(results, key=lambda x: x['year']))

if __name__=='__main__':
    raise SystemExit('Network fetch disabled by default. Deliberately import this module and call corpus() for a NEW snapshot; it cannot restore the historical snapshot.')
