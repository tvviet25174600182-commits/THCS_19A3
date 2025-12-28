# phan_tich.py
from danh_sach import sap_xep_tang_dan
from tu_dien import lay_gia_tri
# Danh sách số
ds = [5, 2, 9, 1, 7]
ds_sap_xep = sap_xep_tang_dan(ds)

print("Danh sách ban đầu:", ds)
print("Danh sách sau khi sắp xếp tăng dần:", ds_sap_xep)

# Từ điển
thong_tin = {
    "ten": "Việt",
    "tuoi": 18,
    "lop": "data science"
}

gia_tri = lay_gia_tri(thong_tin, "tuoi")
print("Giá trị của khóa 'tuoi' là:", gia_tri)
