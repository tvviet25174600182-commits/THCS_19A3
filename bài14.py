A = set(map(int, input().split()))
B = set(map(int, input().split()))

giao = set()
hop = set()
hieuA = set()
hieuB = set()

for x in A:
    if x in B:
        giao.add(x)
    else:
        hieuA.add(x)
    hop.add(x)

for x in B:
    if x not in A:
        hieuB.add(x)
    hop.add(x)

print("A-B:", hieuA)
print("B-A:", hieuB)
print("Giao:", giao)
print("Hợp:", hop)