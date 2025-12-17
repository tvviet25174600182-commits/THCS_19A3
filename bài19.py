d = {'An': 8, 'Bình': 9, 'Chi': 8}
res = {}
for name in d:
    score = d[name]
    if score not in res:
        res[score] = [name]
    else:
        res[score].append(name)
print(res)