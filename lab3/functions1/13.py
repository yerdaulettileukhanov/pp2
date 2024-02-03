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