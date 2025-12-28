with open("nhan_vien.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["ID", "Tên", "Lương"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({"ID": 1, "Tên": "An", "Lương": 45000})
    writer.writerow({"ID": 2, "Tên": "Bình", "Lương": 60000})
    writer.writerow({"ID": 3, "Tên": "Chi", "Lương": 75000})
    writer.writerow({"ID": 4, "Tên": "Dũng", "Lương": 50000})

print("Nhân viên có mức lương trên 50000:\n")

with open("nhan_vien.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if int(row["Lương"]) > 50000:
            print(f"ID: {row['ID']}, Tên: {row['Tên']}, Lương: {row['Lương']}")
