#1
def toOunces(a):
    return 28.3495231 * a

#2
def toC(a):
    return round((5 / 9) * (a - 32), 1)

#3
def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) / 2
    x = numheads - y
    return f"Chickens - {int(x)}, rabbits - {int(y)}"

#4
def isPrime(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt = cnt + 1
    return cnt == 2

def filter(l):
    result = []
    for x in l:
        if isPrime(x):
            result.append(x)
    return result

#5
from itertools import permutations

def per(a):
    b = permutations(a)
    for x in b:
        print(x)

#6
def revStr(a):
    a = list(map(str, a.split()))
    return " ".join(a[::-1])

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#8
def spy_game(a):
    index1 = index2 = None
    for i in range(len(a)):
        if a[i] == 0:
            index1 = i
        elif a[i] == 7:
            index2 = i
    return index1 < index2

#9
def volume(r):
    return round((4 * 3.14 * r ** 3) / 3, 1)

#10
def unique(a):
    box = [None for i in range(len(a))]
    for i in range(len(a)):
        if a[i] not in box:
            box[i] = a[i]
    box = [x for x in box if x is not None]
    return box

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

#12
def histogram(num):
    for x in num:
        print("*" * x)

#13
def guessTheNumber():
    import random
    secret = random.randint(1, 21)
    
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
    i = 1
    cnt = 1
    while(i != 0):
        num = int(input())
        if num > secret:
            print("Your guess is too high.\nTake a guess")
        elif num < secret:
            print("Your guess is too low.\nTake a guess")
        if(num == secret):
            print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
            break
        else:
            cnt += 1