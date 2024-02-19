def squares(a, b):
    while a <= b:
        yield a ** 2
        a += 1

for i in squares(1, 9):
    print(i)