'''
🧩 Problem: Two Sum / K-diff Pairs in an Array
Problem Statement:
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.

⚠️ Constraints
2 <= nums.length <= 10⁴

-10⁹ <= nums[i] <= 10⁹

Only one valid answer exists.

Must return indices, not values.
'''
'''
Brute Force:
def two_sum_K_diff_pair(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return -1
'''
def two_sum_K_diff_pair(nums, target):
    num_to_index = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in num_to_index:
            return [num_to_index[diff], i]
        num_to_index[nums[i]] = i

print(two_sum_K_diff_pair([1, 5, 9, 13, 17, 20], 37))
print(two_sum_K_diff_pair([3, 2, 4, 3], 6))
print(two_sum_K_diff_pair([-3, 4, 3, 90], 0))
print(two_sum_K_diff_pair([2, 7, 11, 15], 9))

'''Main Take Aways: 
- using the target to do math and find out the missing ids that could be in a set.

- using a dictionary to keep track of not only the values in nums but their indeces
'''