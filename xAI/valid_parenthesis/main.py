def valid_parenthesis(ps):

    ps_l = list(ps)
    stk = []

    for i in range(0, len(ps_l)):
        if ps[i] == "(" or ps[i] == "[" or ps[i] == "{":
            stk.append(ps[i])
        else:
            

    return True

print(valid_parenthesis("()[{}]"))
print(valid_parenthesis("([)]"))
print(valid_parenthesis("{[]}"))
