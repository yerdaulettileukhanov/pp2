#1
def toOunces(a):
    return 28.3495231 * a

print(toOunces(int(input())))

#2
def toC(a):
    return round((5 / 9) * (a - 32), 1)

print(toC(int(input())))

#3
def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) / 2
    x = numheads - y
    return f"Chickens - {int(x)}, rabbits - {int(y)}"

a = int(input())
b = int(input())
print(solve(a, b))

#4

#5
from itertools import permutations

def per(a):
    b = permutations(a)
    for x in b:
        print(x)

per(input())

#6
def revStr(a):
    a = list(map(str, a.split()))
    return " ".join(a[::-1])

text = input()
print(revStr(text))

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

n = int(input())
l = []

for i in range(n):
    a = int(input())
    l.append(a)

print(has_33(l))

#8
def spy_game(a):
    index1 = index2 = None
    for i in range(len(a)):
        if a[i] == 0:
            index1 = i
        elif a[i] == 7:
            index2 = i
    return index1 < index2

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#9
def volume(r):
    return round((4 * 3.14 * r ** 3) / 3, 1)

r = int(input())
print(volume(r))

#10
def unique(a):
    box = [None for i in range(len(a))]
    for i in range(len(a)):
        if a[i] not in box:
            box[i] = a[i]
    box = [x for x in box if x is not None]
    return box

print(unique([None, 1, 1, 4, "1", 3, None, 4, "1", 6]))

#11
def palindrome(a):
    j = len(a) - 1
    check = False
    for i in range(round(len(a) / 2)):
        if a[i] == a[j]:
            check = True
            j -= 1
        else:
            check = False
    return check

text = input()
print(palindrome(text))

#12
def histogram(num):
    for x in num:
        print("*" * x)

n = int(input())
l = []

for i in range(n):
    a = int(input())
    l.append(a)

histogram(l)

#13
import random

secret = random.randint(1, 21)

def guessTheNumber(a):
    if a > secret:
        return "Your guess is too high.\nTake a guess"
    elif a < secret:
        return "Your guess is too low.\nTake a guess"
    return f"Good job, {name}! You guessed my number in {cnt} guesses!"

name = input("Hello! What is your name?\n")

print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")

i = 1
cnt = 1
while(i != 0):
    num = int(input())
    print(guessTheNumber(num))
    if("Good job" in guessTheNumber(num)):
        break
    else:
        cnt += 1

#14