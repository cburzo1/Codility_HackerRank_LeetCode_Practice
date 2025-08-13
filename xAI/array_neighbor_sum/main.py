def array_neighbor_sum(arr):
    arr_o = []

    #print(arr[0 -1])

    for i in range(0, len(arr)):
        if i == 0:
            arr_o.append(arr[i] + arr[i + 1])
        elif i == len(arr) - 1:
            arr_o.append(arr[i - 1] + arr[i])
        else:
            arr_o.append(arr[i - 1] + arr[i] + arr[i + 1])

    return arr_o


print(array_neighbor_sum([4, 0, 1, -2, 3]))