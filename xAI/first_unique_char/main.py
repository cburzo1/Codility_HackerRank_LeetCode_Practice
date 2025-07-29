def first_unique_char(s):
    dict_s = {}
    s_l = list(s)

    for i in range(0, len(s_l)):
        if s_l[i] not in dict_s:
            dict_s[s_l[i]] = 1
        else:
            dict_s.update({s_l[i]: dict_s.get(s_l[i]) + 1})

    keys = dict_s.keys()
    first_key = None

    for key in keys:
        if dict_s[key] == 1:
            first_key = key
            break

    if first_key is None:
        return -1
    else:
        return s_l.index(first_key)

print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))
print(first_unique_char("aabbcc"))
print(first_unique_char("aabbc"))
print(first_unique_char("zabcdabc"))
print(first_unique_char("aabbcc"))