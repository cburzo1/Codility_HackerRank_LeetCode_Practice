'''
🧠 Problem: Isomorphic Strings
Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.

No two characters may map to the same character, but a character may map to itself.
'''

'''def isomorphic_strings(s, t):
    s_l = list(s)
    t_l = list(t)

    dict_m = {}

    for i in range(0, len(s_l)):
        if s_l[i] not in dict_m:
            dict_m[s_l[i]] = t_l[i]

    #print(dict_m)

    dict_s = {}
    dict_t = {}

    for i in range(0, len(s_l)):
        if s_l[i] not in dict_s:
            dict_s[s_l[i]] = 1
        else:
            dict_s.update({s_l[i]: dict_s.get(s_l[i]) + 1})

    for i in range(0, len(t_l)):
        if t_l[i] not in dict_t:
            dict_t[t_l[i]] = 1
        else:
            dict_t.update({t_l[i]: dict_t.get(t_l[i]) + 1})

    flag = False

    if len(s) == len(t):
        for i in range(0, len(s_l)):
            if s_l[i] in dict_m and dict_m.get(s_l[i] ) == t_l[i]:
                flag = True
            else:
                flag = False

    #print(dict_m, dict_s, dict_t)

    m_s = set()
    m_t = set()

    key_s = dict_s.keys()
    key_t = dict_t.keys()

    for key in key_s:
        if dict_s.get(key) not in m_s:
            m_s.add(dict_s.get(key))

    for key in key_t:
        if dict_t.get(key) not in m_t:
            m_t.add(dict_t.get(key))

    #print(m_t, m_s)

    if m_t != m_s:
        return False

    return flag'''

def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False

    mapping = {}
    mapped_values = set()

    for sc, tc in zip(s, t):
        if sc not in mapping:
            if tc in mapped_values:
                return False  # One-to-one mapping violated
            mapping[sc] = tc
            mapped_values.add(tc)
        elif mapping[sc] != tc:
            return False

    return True

print(isomorphic_strings("egg", "add")) #True
print(isomorphic_strings("foo", "bar")) # False
print(isomorphic_strings("paper", "title")) #True
print(isomorphic_strings("badc", "baba")) #False
print(isomorphic_strings("abba", "cddc")) # True
print(isomorphic_strings("abba", "cdcd")) #False