import os

os.makedirs("du_an/data", exist_ok=True)
os.makedirs("du_an/output", exist_ok=True)

open("du_an/data/input.txt", "w").close()
open("du_an/output/result.txt", "w").close()
open("du_an/main.py", "w").close()

print("Cấu trúc thư mục và tập tin vừa tạo:\n")

for thu_muc in os.listdir("du_an"):
    duong_dan = os.path.join("du_an", thu_muc)
    print(thu_muc)
    if os.path.isdir(duong_dan):
        for tap_tin in os.listdir(duong_dan):
            print("  ", tap_tin)
