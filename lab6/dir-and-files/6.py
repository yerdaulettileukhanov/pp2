cnt = 65

for i in range(26):
    f = open(f"{chr(cnt)}.txt", "w")
    f.close()
    cnt += 1