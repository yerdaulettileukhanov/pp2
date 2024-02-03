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