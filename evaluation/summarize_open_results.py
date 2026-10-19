"""Recompute the frozen open-data evaluation; no API or private files needed."""
from pathlib import Path
from collections import Counter
import json

BASE = Path(__file__).resolve().parent
def load(name):
    return json.loads((BASE/name).read_text('utf-8'))

cards = load('card_ratings.json')
facts = load('fact_labels.json')
eligible = [r for r in cards if r['identity_eligible']]
contents = load('frozen_card_content.json')
sources = {r['paper_uid']:r['source_text'] for r in load('selected_publication_evidence.json')}
quote_checks = [f['quote'] in sources[f['paper_uid']][:5500] for c in contents for f in c['facts']]
result = {
    'generated_cards':len(cards),
    'generated_people':len({r['person_code'] for r in cards}),
    'selected_papers':len(sources),
    'facts':len(facts),
    'exact_quotes':sum(quote_checks),
    'initial_fact_agreement':sum(r['V-M']==r['V-E'] for r in facts),
    'final_fact_labels':dict(Counter(r['final_label'] for r in facts)),
    'all_rationale_labels':dict(Counter(r['reason_label'] for r in cards)),
    'personal_attribution_flags':sum(r['personal_attribution_flag'] for r in cards),
    'eligible_cards':len(eligible),
    'eligible_people':len({r['person_code'] for r in eligible}),
    'interest':dict(Counter(r['interest'] for r in eligible)),
    'entry':dict(Counter(r['entry'] for r in eligible)),
    'definite_interest_people':len({r['person_code'] for r in eligible if r['interest']=='yes'}),
    'excluded_card_ids':[r['card_id'] for r in cards if not r['identity_eligible']],
    'cells':[],
}
for q in ('T01','T02'):
    for m in ('B1','B2','G'):
        cell = [r for r in eligible if r['query']==q and r['method']==m]
        result['cells'].append({'query':q,'method':m,'eligible':len(cell),
            'definite':sum(r['interest']=='yes' for r in cell),
            'conditional':sum(r['interest']=='conditional' for r in cell),
            'entry_yes':sum(r['entry']=='yes' for r in cell),
            'entry_uncertain':sum(r['entry']=='unknown' for r in cell)})
assert len({r['card_id'] for r in cards}) == len(cards)
assert len({r['item_id'] for r in facts}) == len(facts)
assert {r['card_id'] for r in facts} <= {r['card_id'] for r in cards}
assert len(quote_checks) == len(facts)
assert all(quote_checks)
assert all(r['analysis_included']==r['identity_eligible'] for r in cards)
expected = load('reported_summary.json')['pooled_descriptive']
assert result['eligible_cards']==expected['cards']
assert result['eligible_people']==expected['distinct_candidates']
assert result['definite_interest_people']==expected['yes_unique_candidates']
for key in ('interest','entry'):
    assert all(result[key].get(k,0)==v for k,v in expected[key].items())
(BASE/'recomputed_results.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps(result,indent=2))
