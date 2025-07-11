def sum_equals_k(nums, k):

    tot = 0
    nums_count = 0

    for i in range(0, len(nums)):
        tot += nums[i]

        if tot == k:
            tot -= nums[i - 1]
            nums_count += 1

    return nums_count

print(sum_equals_k([1, 1, 1], 2))
print(sum_equals_k([1, 2, 3], 3))