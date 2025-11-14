so_kwh = int(input("Nhập số kWh điện đã tiêu thụ: "))
bac1 = min(so_kwh, 100) * 1678
bac2 = max(min(so_kwh - 100, 100), 0) * 1734
bac3 = max(min(so_kwh - 200, 100), 0) * 2014
tong_tien = bac1 + bac2 + bac3
print("Tổng số tiền điện phải trả là:", tong_tien)