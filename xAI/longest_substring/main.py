def longest_substring(s):

    s_l = list(s)

    count = 0

    mX = 0

    for i in range(0, len(s_l)):
        for j in range(i + 1, len(s_l)):
            if s_l[i] == s_l[j]:
                count = 0
                break
            else:
                count += 1

            if count > mX:
                mX = count

    return mX


print(longest_substring("abcabcbb"))