def tim_so_le_lon_nhat(a,b,c):
    so_le = [x for x in [a, b, c] if x % 2 != 0]
    if not so_le :
        return -1
    return max(so_le)
a = int(input("nhập a :"))
b = int(input("nhập b :"))
c = int(input("nhập c :"))
ket_qua = tim_so_le_lon_nhat(a , b ,c)
print("số lẻ lớn nhất là :",ket_qua)