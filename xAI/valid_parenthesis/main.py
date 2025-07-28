def valid_parenthesis(ps):

    ps_l = list(ps)
    stk = []

    for i in range(0, len(ps_l)):
        if ps[i] == "(" or ps[i] == "[" or ps[i] == "{":
            stk.append(ps[i])
        else:
            if len(stk) == 0:
                return False

            if stk[len(stk) - 1] == "(" and ps[i] == ")" or  stk[len(stk) - 1] == "{" and ps[i] == "}" or stk[len(stk) - 1] == "[" and ps[i] == "]":
                stk.pop()
            else:
                return False

    return len(stk) == 0

print(valid_parenthesis("()[{}]"))
print(valid_parenthesis("([)]"))
print(valid_parenthesis("{[]}"))
print(valid_parenthesis("()"))         # True
print(valid_parenthesis("()[]{}"))     # True
print(valid_parenthesis("(]"))         # False
print(valid_parenthesis("([)]"))       # False
print(valid_parenthesis("{[]}"))       # True
print(valid_parenthesis("("))          # False
print(valid_parenthesis(")"))          # False
print(valid_parenthesis("((()))"))     # True
print(valid_parenthesis(")("))
