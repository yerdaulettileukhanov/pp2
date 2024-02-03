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