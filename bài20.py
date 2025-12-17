d = {'a': 3, 'b': 7, 'c': 5}
x = int(input("Nhập x: "))

new_d = {}
for k in d:
    if d[k] >= x:
        new_d[k] = d[k]

print(new_d)
