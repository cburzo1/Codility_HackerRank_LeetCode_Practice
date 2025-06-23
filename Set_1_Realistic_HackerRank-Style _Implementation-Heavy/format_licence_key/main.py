import re

def format_licence_key(S, K):
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

    return f_str

format_licence_key("2-4A0r7-4k", 4)
format_licence_key("2-4A0r7-4k", 3)