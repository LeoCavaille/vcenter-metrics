#!/usr/bin/python

import simplejson as json
from all_metrics import ALL_METRICS

def quote(text):
    return "'"+text+"'"

with open('basic_metrics.txt', 'r') as f:
    basic_metrics = f.read().splitlines()

BASIC_METRICS = []

for m in ALL_METRICS:
    if m['name'] in basic_metrics:
        BASIC_METRICS.append(m)

with open('basic_metrics.py', 'w') as f:
    f.write("BASIC_METRICS = [\n")
    for m in BASIC_METRICS:
        m_txt = """    {{
        'name'         : {name},
        's_type'       : {s_type},
        'unit'         : {unit},
        'rollup'       : {rollup},
        'entity'       : {entity}
    }},
""".format(
            name=quote(m['name']),
            s_type=quote(m['s_type']),
            unit=quote(m['unit']),
            rollup=quote(m['rollup']),
            entity=m['entity']
        )
        f.write(m_txt)
    
    f.write("]")
