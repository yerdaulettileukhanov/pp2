def histogram(num):
    for x in num:
        print("*" * x)

n = int(input())
l = []

for i in range(n):
    a = int(input())
    l.append(a)

histogram(l)