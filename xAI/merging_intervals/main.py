def merging_intervals(mx):
    aux = []

    for i in range(1, len(mx)):
        if mx[i - 1][1] >= mx[i][0]:
            aux.append([mx[i - 1][0], mx[i][1]])
        else:
            aux.append(mx[i])

    return aux

print(merging_intervals([[1,3],[2,6],[8,10],[15,18]]))
print(merging_intervals([[1,4],[4,5]]))
print(merging_intervals([[1,3],[2,5],[4,8]]))