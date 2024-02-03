def unique(a):
    box = [None for i in range(len(a))]
    for i in range(len(a)):
        if a[i] not in box:
            box[i] = a[i]
    box = [x for x in box if x is not None]
    return box

print(unique([None, 1, 1, 4, "1", 3, None, 4, "1", 6]))