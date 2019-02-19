import json
data = json.loads(input())

def find_child(parent, ini, results):
    childs = []
    for child in ini:
        if child == parent:
            childs.append(parent['name'])
            continue
        if parent['name'] in child['parents']:
            if child['name'] in results:
                for el in results[child['name']]:
                    if el not in childs:
                        childs.append(el)
                    else:
                        continue
                continue
            if child['name'] not in childs:
                childs.append(child['name'])
            res = find_child(child, ini, results)
            for el in res:
                if el not in childs:
                    childs.append(el)
                else:
                    continue
            continue
        else:
            continue
    results[parent['name']] = childs
    return childs
            
            
results = {}
for parent in data:
    if results.get(parent['name'], 0) != 0:
        continue
    results[parent['name']] = find_child(parent, data, results)

for name in sorted(results):
    print (name, ':', len(results[name]))        
        
