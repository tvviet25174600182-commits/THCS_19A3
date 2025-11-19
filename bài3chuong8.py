import math

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

ucln = math.gcd(tu, mau)
tu_rut = tu // ucln
mau_rut = mau // ucln

print("Phân số rút gọn:", tu_rut, "/", mau_rut)