ten_dang_nhap = input("nhập tên đăng nhập :")
mat_khau = input("Nhập mật khẩu:")
quyen_truy_cap = (ten_dang_nhap == "admin") and (mat_khau != "password123")
print("quyền truy cập hợp lệ: ",quyen_truy_cap)