def revStr(a):
    a = list(map(str, a.split()))
    return " ".join(a[::-1])

text = input()
print(revStr(text))