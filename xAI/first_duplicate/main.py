def first_duplicate(a):
    a_s = set(a)

    if len(a) == len(list(a_s)):
        return -1

    dict_a = {}

    for i in range(len(a)):
        if a[i] not in dict_a:
            dict_a[a[i]] = i

        if a[i] in dict_a and dict_a.get(a[i]) < i:
            return a[dict_a.get(a[i])]

    return -1

print(first_duplicate([2, 1, 3, 5, 3, 2]))
print(first_duplicate([2, 4, 3, 5, 1]))
print(first_duplicate([1, 2, 3, 4, 1, 2, 3]))
print(first_duplicate([1, 2, 3, 4, 5, 6, 2, 1]))
print(first_duplicate([1, 2, 3, 4, 2, 3, 1]) )