def group_word_checker(s):
    s_l = list(s)
    aux = []

    for i in range(0, len(s_l)):
        if s_l[i] not in aux:
            aux.append(s_l[i])

        if s_l[i] in aux and aux[-1] != s_l[i]:
            return False

    return True

print(group_word_checker("aabbcc"))
print(group_word_checker("aabbaa"))
print(group_word_checker("abc"))
print(group_word_checker("a"))
print(group_word_checker("a"))
print(group_word_checker("abca"))
print(group_word_checker("aaabbbcccaaa"))
print(group_word_checker("aba"))

'''
can we use an aux? stack? two pointers? sliding window?
'''