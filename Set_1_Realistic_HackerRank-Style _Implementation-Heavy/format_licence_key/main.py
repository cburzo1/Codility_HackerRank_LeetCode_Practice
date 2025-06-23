import re

def format_license_key(S, K):
    s = re.sub(r'[^a-zA-Z0-9]', '', S).upper()

    arr = []
    count = 0
    temp = ""

    # Go backwards through the string
    for i in range(len(s) - 1, -1, -1):
        temp = s[i] + temp
        count = count + 1

        if count == K:
            arr.insert(0, temp)
            temp = ""
            count = 0
    
    # Add remaining chars if any
    if temp != "":
        arr.insert(0, temp)

    return "-".join(arr)

'''def format_licence_key(S, K):
    f_str = ""

    s = re.sub(r'[^a-zA-Z0-9]', '', S).upper()

    s_div = len(s) / K
    s_mod = len(s) % K

    print(int(s_div))
    if len(s) % K == 0:
        arr = []

        arr.append(s[0:K])
        arr.append(s[K:K + K])

        ns = "-".join(arr)

        print(arr, ns)
    else:
        arr = []

        arr.append(s[0:s_mod])
        arr.append(s[s_mod:K + int(s_mod)])
        arr.append(s[K+int(s_mod):K+int(s_mod)+K])

        ns = "-".join(arr)

        print(arr, ns)

    return f_str'''

format_licence_key("2-4A0r7-4k", 4)
format_licence_key("2-4A0r7-4k", 3)