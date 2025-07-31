def min_window_frequency_match(s, t):

    print(t)

    t.pop(t.index(s[0]))
    t.pop(t.index(s[4]))

    print(t)

    #return []


print(min_window_frequency_match([1, 2, 2, 3, 1, 2, 4], [1, 1,4]))