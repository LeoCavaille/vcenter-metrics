import lxml.html
import sys

def quote(text):
    return "'"+text+"'"

if len(sys.argv) != 3:
    print "Usage transform.py <HTML table file> <metric prefix>"
    sys.exit(1)

filename = sys.argv[1]
stats_type = sys.argv[2]

with open(filename, 'r') as f:
    root = lxml.html.fromstring(f.read())

for br in root.xpath('//br'):
    br.tail = "\n" + br.tail if br.tail else "\n"

print "{0}_METRICS = [".format(stats_type.upper())

for tbl in root.xpath('//table'):
    for row in tbl.xpath('.//tr'):
        raw_elements = row.xpath('.//td')
        elements = [ x.text_content() for x in raw_elements ]
        try:
            a = int(elements[4])
        except (ValueError, IndexError):
            continue

        elements[0] = stats_type + '.' + elements[0]

        print """    # {desc}
    # Compatibility: {compats}
    {{
        'name'         : {name},
        's_type'       : {s_type},
        'unit'         : {unit},
        'rollup'       : {rollup},
        'entity'       : {entity},
        'instance_tag' : None
    }},""".format(
            name=quote(elements[0]),
            s_type=quote(elements[1]),
            unit=quote(elements[2]),
            compats=elements[9].replace('\n', ' / ') if elements[9] else 'UNKNOWN',
            rollup=quote(elements[5].split()[0].strip()),
            entity=elements[7].split(),
            desc=elements[6].strip()
        )
print ']'
