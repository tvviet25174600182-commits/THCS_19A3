def kiem_tra_so_armstrong(n):
    chuoi_so = str(n)
    tong_luy_thua = 0

    for chu_so in chuoi_so:
        chu_so_nguyen = int(chu_so)
        tong_luy_thua += chu_so_nguyen ** 3
    return n == tong_luy_thua
n = int(input("nhập số nguyên dương n :"))
if kiem_tra_so_armstrong(n):
    print("TRUE",n)
else:
    print("FALSE",n)