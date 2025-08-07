def decode_string(s):
    s_l = list(s)
    stk = []

    for i in range(0, len(s_l)):
        if s_l[i] == "]":
            t_s = ""
            s_e = stk.pop()
            while s_e != "[":
                t_s += s_e
                s_e = stk.pop()

            print(t_s[::-1])

            print(stk)

        else:
            stk.append(s_l[i])

print(decode_string("3[a]2[bc]")) # "aaabcbc"
#print(decode_string("3[a2[c]]")) # "accaccacc"
#print(decode_string("2[abc]3[cd]ef")) # "abcabccdcdcdef"
#print(decode_string("10[a]")) # "aaaaaaaaaa"
#print(decode_string("")) # ""
#print(decode_string("2[]")) # ""