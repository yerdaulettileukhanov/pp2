f = open("test.txt", "r")

data = f.read()

cnt = 1

for i in data:
    if i == "\n":
        cnt += 1

print(cnt)