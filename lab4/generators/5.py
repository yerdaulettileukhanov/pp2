def zero(n):
    while n >= 0:
        yield n
        n -= 1

for i in zero(9):
    print(i)