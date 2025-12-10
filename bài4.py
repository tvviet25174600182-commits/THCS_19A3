def tinh_trung_binh_cong(a,b,c):
    trungbinhcong = ( a+b+c)/3
    return trungbinhcong
a = float(input("nhập a :"))
b = float(input("nhập b :"))
c = float(input("nhập c :"))
trungbinhcong = tinh_trung_binh_cong(a,b,c)
print("giá trị trung bình cộng",trungbinhcong)