def kiem_tra_so_doi_xung(n):
    str_n = str(n)
    return str_n[::-1]
n = int(input("nhập số nguyên dương n :"))
if kiem_tra_so_doi_xung(n):
    print(" TRUE",n)
else:
    print("FALSE",n)
