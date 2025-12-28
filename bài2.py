with open("python.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.lower().split()

tan_suat = {}

for word in words:
    if word in tan_suat:
        tan_suat[word] += 1
    else:
        tan_suat[word] = 1

print("Tần suất xuất hiện của các từ: ")
for word, count in tan_suat.items():
    print(f"{word}: {count}")
