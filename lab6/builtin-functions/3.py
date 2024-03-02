text = input()

a = list(reversed(text))

flag = False

for i in range(len(text)):
    if text[i] == a[i]:
        flag = True
    else:
        flag = False

if flag:
    print("Palindrome!")
else:
    print("no!")