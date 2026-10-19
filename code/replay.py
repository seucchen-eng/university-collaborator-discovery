"""Offline reproduction from frozen corpus/similarities and recorded decisions.

No network requests, model inference, new human judgments, or paid API calls.
Run from any directory: python path/to/PREPARATION/code/replay.py
"""
from pathlib import Path
from collections import Counter,defaultdict
import argparse,gzip,hashlib,json,math,platform,runpy,time
import numpy as np
import ranking
import retrieval_rules

PACKAGE=Path(__file__).resolve().parents[1]
F=PACKAGE/'frozen'
def load(path):return json.loads(Path(path).read_text('utf-8'))
def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()
def save(path,value):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n','utf-8')
def rows(path):return list(ranking.rows(path))
def check(condition,name):
    if not condition:raise AssertionError(name)

def main():
    started=time.perf_counter()
    report={'verification_date_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
            'scope':'Offline frozen-input replay; no new model outputs or human judgments',
            'runtime':{'python':platform.python_version(),'numpy':np.__version__},'checks':{}}
    manifest=load(PACKAGE/'corpus_manifest.json')
    h=hashlib.sha256();lines=0
    for part in manifest['parts']:
        check(digest(PACKAGE/part['file'])==part['sha256'],'corpus part digest')
        with gzip.open(PACKAGE/part['file'],'rb') as f:
            for line in f:h.update(line);lines+=1
    check(h.hexdigest()==manifest['original_sha256'],'full original corpus digest')
    check(lines==manifest['rows']==87101,'corpus row count')
    report['checks']['byte_exact_corpus']={'rows':lines,'sha256':h.hexdigest()}

    queries=load(F/'queries.json')
    terms={t for q in queries for t in retrieval_rules.tokens(q['search_text'])}
    stats=[];lengths=[];groups=defaultdict(lambda:{'paper_count':0,'latest_year':0})
    selected_uids={p['uid'] for t in load(F/'selected_candidates.json') for c in t['selected'] for p in c['papers']}
    graph=load(F/'retrieved_graph.json')
    wanted={n['id'] for n in graph['nodes'] if n['type']=='Paper'}|selected_uids
    records={};uids=[];truncated=0;facet_edges=0
    for p in ranking.rows(F/'corpus.jsonl'):
        uids.append(p['paper_uid'])
        check(hashlib.sha256(p['source_text'].encode()).hexdigest()==p['source_text_sha256'],'source text digest')
        check(hashlib.sha256(p['index_text'].encode()).hexdigest()==p['index_text_sha256'],'retrieval text digest')
        check(p['source_text']==p['title']+'\n'+p['abstract'],'source assembly')
        check(p['index_text']==p['source_text'][:p['visible_chars']],'retrieval span')
        check(p['facets']==sorted(k for k,rx in retrieval_rules.RX.items() if rx.search(p['index_text'])),'facet matches')
        truncated+=p['full_wordpieces']>254
        if p['paper_uid'] in wanted:records[p['paper_uid']]=p
        counts=Counter(retrieval_rules.tokens(p['index_text']))
        stats.append({t:counts[t] for t in counts.keys()&terms});lengths.append(sum(counts.values()))
        for key in p['seu_authors']:
            g=groups[key];g['paper_count']+=1;g['latest_year']=max(g['latest_year'],p['year'])
    check(dict(groups)==load(F/'author_eligibility.json'),'all author eligibility counts')
    report['checks']['corpus_fields']={'source_and_index_hashes':2*lines,'signal_sets':lines,
        'truncated_records':truncated,'groups':len(groups),'eligible_groups':sum(g['paper_count']>=2 and g['latest_year']>=2020 for g in groups.values())}
    df=Counter(t for c in stats for t in c);n=len(stats);avgdl=sum(lengths)/n
    bm=np.zeros((len(queries),n),dtype=np.float32)
    for qi,q in enumerate(queries):
        queryterms=set(retrieval_rules.tokens(q['search_text']))
        for i,count in enumerate(stats):
            for t in sorted(queryterms&count.keys()):
                tf=count[t]
                bm[qi,i]+=math.log(1+(n-df[t]+.5)/(df[t]+.5))*tf*2.5/(tf+1.5*(.25+.75*lengths[i]/avgdl))
    original=np.load(F/'bm25_scores.npy')
    check(np.array_equal(bm,original),'BM25 exact float32 array')
    report['checks']['BM25']={'values':bm.size,'array_equal':True,'maximum_absolute_difference':float(np.max(np.abs(bm-original)))}
    del stats,lengths,bm,groups
    dense=np.load(F/'dense_scores.npy')
    check(dense.shape==(2,n) and np.isfinite(dense).all(),'frozen dense score shape')
    expected_dense=load(PACKAGE/'records/retrieval_freeze.json')['hashes']['dense_scores.npy']
    check(digest(F/'dense_scores.npy')==expected_dense,'frozen dense score digest')
    report['checks']['dense_scores']={'values':dense.size,'hash_verified':True,'recomputed_embeddings':False}

    traces,_,pool=ranking.rank()
    check(traces==load(F/'retrieval_trace.json'),'six complete ranking objects')
    report['checks']['ranking']={'cells':len(traces),'ranked_author_rows':sum(len(t['ranked']) for t in traces),
                                'paper_pools':sum(len(t['pool']) for t in traces),'exact_objects':True}
    decisions=load(F/'identity_decisions.json');selection=[];packets=[]
    qs={q['query_id']:q for q in queries}
    for t in traces:
        chosen=[];seen=set();checked=[]
        for r in t['ranked'][:12]:
            d=decisions[r['author_key']]
            valid=d['status']=='verified_for_this_run' and all(p['uid'] in d['verified_paper_uids'] for p in r['papers'])
            duplicate=valid and d['person_id'] in seen
            checked.append({'author_key':r['author_key'],'rank':r['rank'],'status':d['status'],
                            'all_selected_papers_checked':bool(valid),'duplicate_person':bool(duplicate)})
            if not valid or duplicate:continue
            seen.add(d['person_id'])
            chosen.append({**r,**{k:d[k] for k in ['person_id','name','college','profile_url']},'candidate_id':d['person_id']})
            if len(chosen)==3:break
        selection.append({'query_id':t['query_id'],'method':t['method'],'checked_until_stop':checked,'selected':chosen})
        packets.append({'query_id':t['query_id'],'method':t['method'],
            'packet':{'query_id':t['query_id'],'need':qs[t['query_id']]['need'],'candidates':[
                {'candidate_id':c['candidate_id'],'papers':[{'paper_uid':p['uid'],'source_text':records[p['uid']]['source_text'][:5500]} for p in c['papers']]}
                for c in chosen]}})
    check(selection==load(F/'selected_candidates.json'),'identity gate replay')
    check(packets==rows(F/'inference_inputs.jsonl'),'six generation inputs')
    report['checks']['identity_and_inputs']={'selected_cards':sum(len(s['selected']) for s in selection),
        'reviewed_group_instances':sum(len(s['checked_until_stop']) for s in selection),
        'input_packets_exact':6,'scope':'Replays recorded operational decisions; does not revalidate personal identity.'}
    node_ids={n['id'] for n in graph['nodes']}
    for e in graph['edges']:
        check(e['source'] in node_ids and e['target'] in node_ids,'graph endpoints')
        if e['relation']=='MENTIONS':
            p=records[e['source']]
            check(p['index_text'][e['start']:e['end']]==e['quote'],'graph span')
            rx=retrieval_rules.RX[e['target'].split(':',1)[1]];m=rx.search(p['index_text'])
            check((m.start(),m.end(),m.group())==(e['start'],e['end'],e['quote']),'graph rule')
            facet_edges+=1
        elif e['relation']=='COAUTHORED':
            check(records[e['target']]['seu_authors'][e['source'].split(':',1)[1]]==e['raw_authorship'],'graph authorship')
    report['checks']['graph']={'nodes':len(graph['nodes']),'edges':len(graph['edges']),'exact_signal_spans':facet_edges}

    outs=rows(F/'outputs.jsonl');ledger=rows(F/'api_ledger.jsonl');reserved={r['request_id']:r for r in ledger if r['event']=='reserved'}
    packet_by={(r['query_id'],r['method']):r['packet'] for r in packets};facts=0;quotes=0
    for o in outs:
        rid=o['request_id'];request=load(F/('request_'+rid+'.json'));response=load(F/('response_'+rid+'.json'))
        check(digest(F/('request_'+rid+'.json'))==reserved[rid]['request_sha256'],'retained HTTP request hash')
        check(request['messages'][0]['content']==(F/'prompt.txt').read_text('utf-8'),'system prompt')
        check(json.loads(request['messages'][1]['content'])==packet_by[o['query_id'],o['method']],'request content')
        check(json.loads(response['choices'][0]['message']['content'])==o['output'],'retained HTTP response content')
        for c in o['output']['candidates']:
            for f in c['facts']:
                facts+=1;check(f['quote'] in records[f['paper_uid']]['source_text'][:5500],'exact quote');quotes+=1
    report['checks']['generation_records']={'requests':len(outs),'responses':len(outs),'facts':facts,'exact_quotes':quotes,'new_api_calls':0}

    runpy.run_path(str(PACKAGE/'evaluation/summarize_open_results.py'),run_name='__main__')
    report['checks']['human_aggregation']=load(PACKAGE/'evaluation/recomputed_results.json')
    report['all_passed']=True;report['seconds']=time.perf_counter()-started
    save(PACKAGE/'verification/offline_replay.json',report)
    print(json.dumps({'all_passed':True,'ranked_author_rows':report['checks']['ranking']['ranked_author_rows'],
                      'BM25_values':2*n,'seconds':report['seconds']},indent=2))
if __name__=='__main__':main()
