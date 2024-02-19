def div(n):
    start = 0
    while start <= n:
        if start % 12 == 0:
            yield start
        start += 1

for i in div(84):
    print(i)