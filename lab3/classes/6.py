def isPrime(nums):
    cnt = 0
    for i in range(1, nums + 1):
        if nums % i == 0:
            cnt += 1
    if cnt == 2:
        return True

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 77, 97, 103, 17, 23]

a = list(filter(isPrime, l))

print(a)