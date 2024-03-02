import time

a = int(input("Number: "))
b = int(input("Time: "))

print(f"Square root of {a} after {b} miliseconds is: ")

time.sleep(b / 1000)
print(a ** (0.5))