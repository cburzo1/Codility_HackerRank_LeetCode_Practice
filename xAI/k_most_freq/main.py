def k_most_freq(nums, k):
    dict_n = {}

    for i in range(0, len(nums)):
        if nums[i] not in dict_n:
            dict_n[nums[i]] = 1
        else:
            dict_n.update({nums[i]:dict_n.get(nums[i]) + 1})

    keys = dict_n.keys()
    values = dict_n.values()

    keys_l = list(keys)
    values_l = list(values)

    for j in range(len(values_l) - 1, -1, -1):
        for i in range(1, j):
            if values_l[i] > values_l[i - 1]:
                temp = keys_l[i]
                keys_l[i] = keys_l[i - 1]
                keys_l[i - 1] = temp

                temp = values_l[i]
                values_l[i] = values_l[i - 1]
                values_l[i - 1] = temp

    i = 0
    col = []

    while i < k:
        col.append(keys_l[i])
        i += 1

    return col

print(k_most_freq([1,1,1,2,2,3], 2))
print(k_most_freq([4,4,4,4,5,5,6], 1))
print(k_most_freq([1,1,1,2,3,4,4,4,4,4,5,5], 3))
