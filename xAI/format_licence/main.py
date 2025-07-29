import re

def format_license(s, t):
    #print(s, t)
    s_f = re.sub(r'[^a-zA-Z0-9]', '', s).upper()

    count = 0

    s2 = ""

    for i in range(len(s_f) - 1, -1, -1):
        count += 1
        s2 = s_f[i] + s2
        if count == t:
            s2 = "-" + s2
            count = 0

    if s2[0] == '-':
        return s2[1:]
    else:
        return s2

print(format_license("5F3Z-2e-9-w", 4))
print(format_license("2-5g-3-J", 2))
print(format_license("abc", 1))