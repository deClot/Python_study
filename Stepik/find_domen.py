import requests
import re

A = input().rstrip()
res_a = requests.get(A).text

template = r'<a.*href=["\'](.*)["\'].*>'

a_ref = re.findall(template, res_a)

result = []
protocol = r'[a-zA-Z]*://([\w-]+(\.[\w-]+)*)'
path = r'\.\./.*()'
not_protocol = r'([\w-]+(\.[\w-]+)+)'
    
templates = [protocol, path, not_protocol]
for link in a_ref:
    for temp in templates:
        try:
            domen = re.match(temp, link)[1]
            if domen not in result and domen != '':
                result.append(domen)
        except TypeError:
            continue
    
for el in sorted(result):
    print (el)
