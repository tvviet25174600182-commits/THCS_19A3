import sys
import os

duong_dan_thu_vien = os.path.abspath("bai5C12_thu_vien_chung")

sys.path.append(duong_dan_thu_vien)

import xu_li_so

so = 11
ket_qua = xu_li_so.kiem_tra_so_nguyen_to(so)

print(f"Số {so} là số nguyên tố:", ket_qua)
