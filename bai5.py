so_tien_gui_ban_dau = float(input("Nhập số tiền gửi ban đầu:"))
lai_suat_nam = float(input("Nhập lãi suất năm:"))
lai_suat_thang = so_tien_gui_ban_dau * lai_suat_nam * 1/12
lai_suat_2quy = so_tien_gui_ban_dau * lai_suat_nam * 1/2
lai_suat_3nam = so_tien_gui_ban_dau * lai_suat_nam * 3
print("lãi suất 1 tháng: ",lai_suat_thang)
print("lãi suất 2 quý: ",lai_suat_2quy)
print("lãi suất 3 năm: ",lai_suat_3nam)