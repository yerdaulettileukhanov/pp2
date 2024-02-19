import math

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
apothem = l / (2 * math.tan(math.radians(180) / n))

print("The area of the polygon is:", round((n * l * apothem) / 2))