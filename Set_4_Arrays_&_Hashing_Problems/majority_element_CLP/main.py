'''
SET 4
🧩 Majority Element
Problem Statement:

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.

You may assume that the majority element always exists in the array.

Constraints:

n == nums.length

1 <= n <= 5 * 10^4

-10^9 <= nums[i] <= 10^9

The majority element always exists in the input.
'''

def majority_element(nums):
    nums_s = set(nums)
    nums_l = list(nums_s)
    dict_n = {}

    for i in range(0, len(nums_l)):
        dict_n[nums_l[i]] = 0

    for i in range(0, len(nums)):
        dict_n.update({nums[i]:dict_n.get(nums[i]) + 1})

    print(dict_n)

    keys = dict_n.keys()

    max_n = 0
    majority_elem = None

    for key in keys:
        if dict_n[key] > max_n:
            max_n = dict_n[key]
            majority_elem = key

    return majority_elem

print(majority_element([2,2,1,1,1,2,2]))
print(majority_element([3, 3, 4]))
print(majority_element([1, 2, 3, 2, 2, 2, 2]))
print(majority_element([9, 9, 9, 9, 9]))
print(majority_element([8, 1, 8, 2, 8, 3, 8]))

'''Main Take Aways: 
- using a set to populate the keys of a dict.

- O(1) solution exits called Boyer-Moore Voting. But its useless beyond this use case.
'''