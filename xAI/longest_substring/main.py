'''def longest_substring(s):
    s_l = list(s)
    count = 0
    biggest = 0
    aux_a = []

    for i in range(0, len(s_l)):
        if s_l[i] not in aux_a:
            aux_a.append(s_l[i])
            count += 1
        else:
            aux_a.pop(aux_a.index(s_l[i]))
            count = 0

        if count > biggest:
            biggest = count

    return biggest'''

def longest_substring(s):
    s_l = list(s)
    count = 0
    biggest = 0
    aux_a = []

    for i in range(len(s_l)):
        if s_l[i] not in aux_a:
            aux_a.append(s_l[i])
            count += 1
        else:
            # Remove up to and including the first occurrence of the repeated character
            repeat_index = aux_a.index(s_l[i])
            aux_a = aux_a[repeat_index + 1:] + [s_l[i]]
            count = len(aux_a)

        if count > biggest:
            biggest = count

    return biggest

print(longest_substring("abcabcbb"))
print(longest_substring("bbbb"))
print(longest_substring("pwwkew"))
print(longest_substring("abccba"))
print(longest_substring("aabcbcbb"))