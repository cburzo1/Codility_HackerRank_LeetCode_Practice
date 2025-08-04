def first_unique_char(s):
    s_l = list(s)
    dict_c = {}

    for i in range(0, len(s_l)):
        if s_l[i] not in dict_c:
            dict_c[s_l[i]] = 1
        else:
            dict_c.update({s_l[i]:dict_c.get(s_l[i]) + 1})

    keys = dict_c.keys()

    for key in keys:
        if dict_c[key] == 1:
            return s_l.index(key)

    return -1

print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))


