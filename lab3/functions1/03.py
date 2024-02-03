def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) / 2
    x = numheads - y
    return f"Chickens - {int(x)}, rabbits - {int(y)}"

a = int(input())
b = int(input())
print(solve(a, b))