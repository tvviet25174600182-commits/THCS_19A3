d = {'a': 1, 'b': 2}
new_d = {}

for k in d:
    new_d[d[k]] = k

print(new_d)