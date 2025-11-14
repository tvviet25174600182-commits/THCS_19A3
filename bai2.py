so_keo = int(input("Nhập số kẹo:"))
so_hoc_sinh = int (input("Nhập số học sinh:"))
so_keo_moi_hoc_sinh_nhan_duoc = so_keo // so_hoc_sinh
so_keo_con_thua = so_keo % so_hoc_sinh
print("số kẹo mỗi học sinh nhận được là: ",so_keo_moi_hoc_sinh_nhan_duoc)
print("số kẹp còn thừa: ",so_keo_con_thua)