luong_co_ban = float(input("Nhập mức lương cơ bản: "))
so_ngay_cong = int(input("Nhập số ngày công trong tháng: "))
luong_ngay = luong_co_ban / 22
luong_thuc_nhan = luong_ngay * so_ngay_cong
thuong = luong_co_ban * 0.10 * (so_ngay_cong > 22)
phat = luong_co_ban * 0.05 * (so_ngay_cong < 22)
tong_luong = luong_thuc_nhan + thuong - phat
print("Tổng lương phải trả:", tong_luong)