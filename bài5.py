import os

nguon = "tep_nguon.bin"
dich = "tep_dich.bin"

if not os.path.exists(nguon):
    print("Tập tin nguồn không tồn tại!")
else:
    with open(nguon, "rb") as f_nguon:
        with open(dich, "wb") as f_dich:
            while True:
                data = f_nguon.read(1024)
                if not data:
                    break
                f_dich.write(data)

    print("Sao chép tập tin thành công!")

