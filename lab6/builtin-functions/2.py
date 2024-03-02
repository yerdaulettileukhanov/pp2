text = input()

lowerCase = 0
upperCase = 0

for i in text:
    if i.islower():
        lowerCase += 1
    elif i.isupper():
        upperCase += 1

print(f"Number of upper cases: {upperCase}\nNumber of lower cases: {lowerCase}")