a = list(map(int, input("Nhập list: ").split()))
k = int(input("Nhập k: "))

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == k:
            print(a[i], a[j])