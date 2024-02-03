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