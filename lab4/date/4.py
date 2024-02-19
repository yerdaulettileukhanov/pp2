import datetime

a = input("Enter year, month, day, hour, minute, and second of first date: ")
b = input("Enter year, month, day, hour, minute, and second of second date: ")

l1 = list(map(int, a.split()))
l2 = list(map(int, b.split()))

x = datetime.datetime(l1[0], l1[1], l1[2], l1[3], l1[4], l1[5])
y = datetime.datetime(l2[0], l2[1], l2[2], l2[3], l2[4], l2[5])

print(x.second - y.second)