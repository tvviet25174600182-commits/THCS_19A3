gia_san_pham = float(input("Nhập giá sản phẩm:"))
so_luong = int(input("Nhập số lượng:"))
tong_chi_phi = gia_san_pham * so_luong
VAT = tong_chi_phi * 0.10
tong_tien = tong_chi_phi + VAT
print("Nhập tổng tiền: {:.2f}".format(tong_tien))