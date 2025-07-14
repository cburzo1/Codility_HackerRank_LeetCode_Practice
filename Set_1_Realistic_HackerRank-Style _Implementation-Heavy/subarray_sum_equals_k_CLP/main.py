'''
SET 1
🧩 3. Subarray Sum Equals K
Problem Statement:

Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Constraints:

1 <= nums.length <= 2 * 10^4

-1000 <= nums[i] <= 1000

-10^7 <= k <= 10^7
'''

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

def sum_equals_k(nums, k):
    prefix_counts = {0: 1}  # We’ve seen sum 0 once (important!)
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num
        diff = prefix_sum - k

        if diff in prefix_counts:
            count += prefix_counts[diff]

        # Handle new or existing prefix_sum keys
        if prefix_sum in prefix_counts:
            prefix_counts[prefix_sum] += 1
        else:
            prefix_counts[prefix_sum] = 1

    return count

print(sum_equals_k([1, 1, 1], 2))
print(sum_equals_k([1, 2, 3], 3))
print(sum_equals_k([1, -1, 1, 1, 1], 2))
print(sum_equals_k([-1, -1, -1], -2))
print(sum_equals_k([3, 4, 7, 2, -3, 1, 4, 2],7))

'''
Main Take Aways: 

- prefix sum with two pointers only works for positive integers; this works for negative and positive

- Brute force might be too slow for some test cases, so the optimal solution should be the one that
is focused on the most
'''