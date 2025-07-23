'''
SET 4
🔹 Problem: Intersection of Two Arrays
Leetcode Link: 349. Intersection of Two Arrays

🧠 Problem Statement:
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in
the result must be unique and you may return the result in any order.
'''
'''
brute force

def intersection_of_two_arrays(nums1, nums2):
    nums_r = []
    nums1_s = set(nums1)
    nums2_s = set(nums2)
    nums1_l = list(nums1_s)
    nums2_l = list(nums2_s)

    for i in range(0, len(nums1_l)):
        for j in range(0, len(nums2_l)):
            if nums1_l[i] == nums2_l[j]:
                nums_r.append(nums1_l[i])

    return nums_r
'''

def intersection_of_two_arrays(nums1, nums2):
    nums_r = []
    nums1_s = set(nums1)
    nums2_s = set(nums2)

    for i in nums1_s:
        if i in nums2_s:
            nums_r.append(i)

    return nums_r

print(intersection_of_two_arrays([1, 2, 2, 1], [2, 2]))
print(intersection_of_two_arrays([4,9,5], [9,4,9,8,4]))