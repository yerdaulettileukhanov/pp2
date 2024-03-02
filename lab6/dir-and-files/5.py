a = [89, 100, 53, 19, 37]

f = open("list.txt", "w")

for i in a:
    f.write(str(i) + " ")

f.close()