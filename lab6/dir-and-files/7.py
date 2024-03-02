f1 = open("text.txt", "r")
f2 = open("test.txt", "w")

data = f1.read()
f2.write(data)

f1.close()
f2.close()