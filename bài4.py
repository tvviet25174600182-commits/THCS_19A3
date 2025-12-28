noi_dung = """ID, Tên sản phẩm, Giá
1, Laptop, 1200
2, Chuột máy tính, 25
3, Bàn phím, 75
"""

with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write(noi_dung)

id_can_cap_nhat = input("Nhập ID sản phẩm cần cập nhật giá: ")

gia_moi = input("Nhập giá mới: ")

ds_moi = []

with open("san_pham.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if line.startswith("ID"):
        # Giữ nguyên dòng tiêu đề
        ds_moi.append(line)
    else:
        parts = line.split(", ")
        if parts[0] == id_can_cap_nhat:
            # Cập nhật giá mới
            parts[2] = gia_moi
            ds_moi.append(", ".join(parts))
        else:
            ds_moi.append(line)

with open("san_pham.txt", "w", encoding="utf-8") as f:
    for dong in ds_moi:
        f.write(dong + "\n")

print("Đã cập nhật giá sản phẩm thành công!")
