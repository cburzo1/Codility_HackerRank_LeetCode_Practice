'''import re

def valid_palindrome(s):
    s2 = re.sub(r'[^a-zA-Z0-9]','', s).lower()
    s2_l = list(s2)

    i = 0
    j = len(s2_l) - 1

    while i < j:
        temp = s2_l[i]
        s2_l[i] = s2_l[j]
        s2_l[j] = temp
        i += 1
        j -= 1

    if s2 == "".join(s2_l):
        return True
    else:
        return False

print(valid_palindrome("A man, a plan, a canal: Panama"))
print(valid_palindrome("race a car"))'''

import re

def valid_palindrome(s):
    s2 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    s2_l = list(s2)
    original = s2  # Save for comparison

    i = 0
    j = len(s2_l) - 1

    while i < j:
        temp = s2_l[i]
        s2_l[i] = s2_l[j]
        s2_l[j] = temp
        i += 1
        j -= 1

    reversed_str = "".join(s2_l)

    return original == reversed_str

print(valid_palindrome("A man, a plan, a canal: Panama"))
print(valid_palindrome("race a car"))