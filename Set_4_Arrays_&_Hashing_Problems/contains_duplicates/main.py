'''
🧩 Problem: Contains Duplicate
Prompt:
Given an integer array nums, return true if any value appears at least twice, and return false if every element is distinct.

🔒 Constraints:
1 <= nums.length <= 10⁵

-10⁹ <= nums[i] <= 10⁹
'''

def contains_duplicates(nums):
    seen = set()  # Correctly initialize a set

    for num in nums:
        if num in seen:
            return True  # Found a duplicate
        seen.add(num)

    return False  # No duplicates found