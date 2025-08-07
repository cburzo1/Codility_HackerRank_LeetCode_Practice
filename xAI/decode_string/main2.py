def decode_string(s):
    s_l = list(s)
    stack = []

    curr_num = 0
    curr_str = ""

    for i in range(0, len(s_l)):
        char = s_l[i]

        if char.isdigit():
            curr_num = curr_num * 10 + int(char)

        elif char == "[":
            # Push current string and number to stack
            stack.append(curr_str)
            stack.append(curr_num)
            # Reset current string and number
            curr_str = ""
            curr_num = 0

        elif char == "]":
            # Pop number and previous string
            num = stack.pop()
            prev_str = stack.pop()
            # Repeat current string and append to previous
            curr_str = prev_str + curr_str * num

        else:
            # It's a character
            curr_str += char

    return curr_str

print(decode_string("3[a]2[bc]")) # "aaabcbc"
print(decode_string("3[a2[c]]")) # "accaccacc"
print(decode_string("2[abc]3[cd]ef")) # "abcabccdcdcdef"
print(decode_string("10[a]")) # "aaaaaaaaaa"
print(decode_string("")) # ""
print(decode_string("2[]")) # ""