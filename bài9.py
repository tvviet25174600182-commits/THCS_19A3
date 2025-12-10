def tinh_tong_chu_so(n):
    if n < 10:
        return n
    return n % 10 + tinh_tong_chu_so(n // 10)
n = int(input("nhập số nguyên dương n :"))
tong = tinh_tong_chu_so(n)
print("tổng các chữ số là :", tong)