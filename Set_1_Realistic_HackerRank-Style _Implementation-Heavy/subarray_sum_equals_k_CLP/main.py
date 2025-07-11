'''
Brute Force:
def sum_equals_k(nums, k):

    tot = 0
    nums_count = 0

    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            tot += nums[j]

            if tot == k:
                nums_count += 1

        tot = 0

    return nums_count'''

'''
My Attempt at Optimal
def sum_equals_k(nums, k):
    nums_count = 0
    tot = 0
    i = 0
    j = 1
    while i < j:
        tot += nums[j]

        if tot == k:
            i += 1
            tot -= nums[i]
            nums_count += 1
        j += 1

    return nums_count
'''

print(sum_equals_k([1, 1, 1], 2))
print(sum_equals_k([1, 2, 3], 3))
print(sum_equals_k([1, -1, 1, 1, 1], 2))
print(sum_equals_k([-1, -1, -1], -2))
print(sum_equals_k([3, 4, 7, 2, -3, 1, 4, 2],7))