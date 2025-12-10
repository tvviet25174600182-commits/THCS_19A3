def giai_phuong_trinh_bac_nhat(a, b):
    if b == 0:
        if a == 0:
            return "vô số nghiệm"
        else:
            return "vô nghiệm"
    else:
        return "-b/a"
print(giai_phuong_trinh_bac_nhat(2, 4))     