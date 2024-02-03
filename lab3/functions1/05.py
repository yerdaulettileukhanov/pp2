from itertools import permutations

def per(a):
    b = permutations(a)
    for x in b:
        print(x)

per(input())