print("sinh vien : nguyen sy anh viet ")

print("ma so sv :245751030110042")

print("#############################")
ds = input("Nhập dãy từ: ").split()

maxlen = max(len(t) for t in ds)

for t in ds:
    if len(t) == maxlen:
        print(t)

