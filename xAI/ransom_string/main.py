def ransom_string(r, m):

    dict_r = {}
    dict_m = {}

    r_l = list(r)
    m_l = list(m)

    for i in range(0, len(r_l)):
        if r_l[i] not in dict_r:
            dict_r[r_l[i]] = 1
        else:
            dict_r.update({r_l[i]: dict_r.get(r_l[i]) + 1})

    for i in range(0, len(m_l)):
        if m_l[i] not in dict_m:
            dict_m[m_l[i]] = 1
        else:
            dict_m.update({m_l[i]: dict_m.get(m_l[i]) + 1})

    keys_r = dict_r

    for key in keys_r:
        if key in dict_m:
            if dict_r[key] > dict_m[key]:
                print(dict_r[key], dict_m[key])
                return False
        else:
            return False

    return True

print(ransom_string("a", "b")) #False
print(ransom_string("aa", "ab")) #False
print(ransom_string("aa", "aab")) #True
print(ransom_string("aabbcc", "abcabc")) #True
print(ransom_string("aabbcc", "aabbbc")) #False
print(ransom_string("aaab", "aabcde")) #False
print(ransom_string("aa", "aaa")) #True