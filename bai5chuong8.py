n = int(input("Nhập n: "))
S1 = sum(range(1, n+1))
print("S1 =", S1)

n = int(input("Nhập n: "))
S2 = 1
for i in range(1, n):
    S2 *= i
print("S2 =", S2)

n = int(input("Nhập n: "))
S3 = 0
for i in range(1, n+1):
    S3 += ((-1)**(i+1)) / i
print("S3 =", S3)

n = int(input("Nhập n: "))
S4 = 0
for k in range(0, n+1):
    S4 += k / (k + 2)
print("S4 =", S4)