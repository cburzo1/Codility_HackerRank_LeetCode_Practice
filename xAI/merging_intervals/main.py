def merging_intervals(mx):
    aux = []

    '''for i in range(1, len(mx)):
        if mx[i - 1][1] >= mx[i][0]:
            aux.append([mx[i - 1][0], mx[i][1]])
        else:
            aux.append(mx[i])'''

    #sort by y
    for i in range(len(mx), -1, -1):
        for j in range(1, i):
            if mx[j - 1][1] > mx[j][1]:
                temp = mx[j]
                mx[j] = mx[j - 1]
                mx[j - 1] = temp

    print(mx)

    # start at mx[0] and only check the next pair, if the next pair doesnt pass,
    # merge stay on this index though and check the next one, only moving on if it passes

    return aux

print(merging_intervals([[2,6],[1,3],[9,18],[5,10]])) # always check next before advancing
# [1,6] [5, 10] [9, 18] -> [1,10], [9,18] -> [1, 18]
#print(merging_intervals([[1,4],[4,5]]))
#print(merging_intervals([[1,3],[4,8],[2,5]]))