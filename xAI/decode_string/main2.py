def decode_string(s):
    print(s)

print(decode_string("3[a]2[bc]")) # "aaabcbc"
print(decode_string("3[a2[c]]")) # "accaccacc"
print(decode_string("2[abc]3[cd]ef")) # "abcabccdcdcdef"
print(decode_string("10[a]")) # "aaaaaaaaaa"
print(decode_string("")) # ""
print(decode_string("2[]")) # ""