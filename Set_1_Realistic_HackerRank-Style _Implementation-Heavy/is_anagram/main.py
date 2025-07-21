'''
Brute Force

def is_anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    s1_l = list(s1)
    s2_l = list(s2)

    for i in range(0, len(s1_l)):
        for j in range(0, len(s2_l)):
            if s1_l[i] == s2_l[j]:
                s2_l.pop(j)
                break

    if len(s2_l) == 0:
        return True
    else:
        return False
'''

def is_anagram(s1, s2):
    dict_n = {}
    dict_t = {}

    s1_l = list(s1)
    s2_l = list(s2)

    for i in range(0, len(s1_l)):
        if s1_l[i] not in dict_n:
            dict_n[s1_l[i]] = 1
        else:
            dict_n.update({s1_l[i]:dict_n.get(s1_l[i]) + 1})

    for i in range(0, len(s2_l)):
        if s2_l[i] not in dict_t:
            dict_t[s2_l[i]] = 1
        else:
            dict_t.update({s2_l[i]:dict_t.get(s2_l[i]) + 1})

    if dict_n == dict_t:
        return True
    else:
        return False

print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("aacc", "ccac"))