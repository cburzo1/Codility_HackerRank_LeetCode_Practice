def majority_element(nums):
    nums_s = set(nums)

    print(nums_s)

    nums_l = list(nums_s)

    dict_n = {}

    for i in range(0, len(nums_l)):
        dict_n[nums_l[i]] = 0

    for i in range(0, len(nums)):
        dict_n.update({nums[i]:dict_n.get(nums[i]) + 1})

    print(dict_n)

    keys = dict_n.keys()

    max_n = 0

    for key in keys:
        if dict_n[key] > max_n:
            max_n = dict_n[key]

    return max_n

print(majority_element([2,2,1,1,1,2,2]))