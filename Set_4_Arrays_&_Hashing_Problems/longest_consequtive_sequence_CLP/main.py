'''
SET 4
🔷 Problem: Longest Consecutive Sequence
Given an unsorted array of integers nums,
return the length of the longest sequence of consecutive elements.

You must write an algorithm that runs in O(n) time.

🔸 Constraints:
0 <= nums.length <= 10⁵

-10⁹ <= nums[i] <= 10⁹
'''

'''
MY ATTEMPT:

def longest_cons_seq(arr):
    num = 0

    m = max(arr)

    h = [0] * (m + 1)

    for i in range(0, len(arr)):
        h[arr[i]] = 1

    count = 0

    for i in range(0, len(h)):
        if h[i] == 1:
            count += 1
        else:
            count = 0

        if count > num:
            num = count

    return num

'''

def longest_cons_seq(nums):
    # Step 1: Store all numbers in a set for O(1) lookups
    num_set = set()
    for i in range(0, len(nums)):
        num_set.add(nums[i])

    longest = 0

    # Step 2: Iterate through each number
    for i in range(0, len(nums)):
        current_num = nums[i]

        # Only start counting if it's the start of a sequence
        if (current_num - 1) not in num_set:
            count = 1
            next_num = current_num + 1

            # Count consecutive numbers
            while next_num in num_set:
                count += 1
                next_num += 1

            # Update the max length
            if count > longest:
                longest = count

    return longest


print(longest_cons_seq([100, 4, 200, 1, 3, 2]))
print(longest_cons_seq([0,3,7,2,5,8,4,6,0,1]))
print(longest_cons_seq([1, 2, 2, 2, 3, 3]))

'''Main Take Aways: 
- My Solution uses readable explicit hash arrays. PROBLEM WITH MY ATTEMPT: It does not work for
negative numbers without tediously altering the list to put 0 in the middle and then use math to
offset the index. A better solution would be one that uses set()

- understand how set() uses a fundamental hashing principle and hash() method to add data. It is
open addressing collision resolution.

'''