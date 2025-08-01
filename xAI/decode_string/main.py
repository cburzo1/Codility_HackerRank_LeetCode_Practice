def decode_string(s):
    s_l = list(s)
    dict_e = {}
    s2n = ""

    for i in range(0, len(s_l)):
        if s_l[i].isdigit():
            s2n += s_l[i]

        if s_l[i] == '[':
            j = i+1
            s2 = ""
            while s_l[j] != ']':
                s2 += s_l[j]
                j += 1

            if s2 not in dict_e:
                dict_e[s2] = s2n

            s2n = ""

    keys = dict_e.keys()
    s3 = ""

    for key in keys:
        i = int(dict_e.get(key))
        j = 0
        while j < i:
            s3 += key
            j+=1

    if s_l[len(s_l) - 1] != "]":
        s5 = ""
        i = len(s_l) - 1
        while s_l[i] != "]":
            s5 += s_l[i]
            i-= 1

        s3 = s3 + s5[::-1]

    return s3

'''print(decode_string("3[a]2[bc]"))
print(decode_string("3[a2[c]]"))
print(decode_string("2[abc]3[cd]ef"))
print(decode_string("10[z]"))
print(decode_string("3[x]2[]1[y]"))
print(decode_string("4[mn]1[o]"))'''
print(decode_string("2[ab]3[cd]"))       # ababcddcd
print(decode_string("2[ab]c3[d]"))       # ababcddd
print(decode_string("10[x]y"))           # xxxxxxxxxxy
print(decode_string("2[hello]world"))