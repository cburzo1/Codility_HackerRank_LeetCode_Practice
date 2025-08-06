def is_valid_bracket_sequence(s):
    s_l = list(s)

    stk = []

    for i in range(0, len(s_l)):
        if s_l[i] == "(" or s_l[i] == "{" or s_l[i] == "[":
            stk.append(s_l[i])
        else:
            if len(stk) == 0:
                return False

            if s_l[i] == ")" and stk[-1] == "(" or s_l[i] == "}" and stk[-1] == "{" or s_l[i] == "]" and stk[-1] == "[":
                stk.pop()

    return len(stk) == 0

print(is_valid_bracket_sequence("()[]{}"))      # ➞ True
print(is_valid_bracket_sequence("(]"))         # ➞ False
print(is_valid_bracket_sequence("([{}])"))     # ➞ True
print(is_valid_bracket_sequence("((()))[]{}")) # ➞ True
print(is_valid_bracket_sequence("({[)]}"))     # ➞ False