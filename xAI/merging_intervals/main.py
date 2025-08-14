def merging_intervals(mx):
    aux = []

    for i in range(len(mx), -1, -1):
        for j in range(1, i):
            if mx[j - 1][1] > mx[j][1]:
                temp = mx[j]
                mx[j] = mx[j - 1]
                mx[j - 1] = temp

    aux.append(mx[0])
    count = 0

    for i in range(1, len(mx)):
        if aux[count][1] >= mx[i][0]:
            aux[count][1] = mx[i][1]
        else:
            aux.append(mx[i])
            count += 1

    return aux

print(merging_intervals([[1,3],[2,6],[5,10], [11,18]])) # always check next before advancing
# [1,6] [5, 10] [9, 18] -> [1,10], [9,18] -> [1, 18]
print(merging_intervals([[1,4],[4,5]]))
print(merging_intervals([[1,3],[4,8],[2,5]])) #[1,3][4,5]
print(merging_intervals([[1, 3], [2, 4], [5, 7]])) #[1,4][5,7]
print(merging_intervals([[1, 2], [2, 3], [3, 4]])) #[1,4]
print(merging_intervals([[2, 5],[6, 9], [1, 10]])) #[2,5][6,10]
print(merging_intervals([[1, 2], [4, 5], [7, 8]])) #[]

'''if aux[count][1] >= mx[1][0]:
      aux[count][1] = mx[1][1]
  else:
      aux.append(mx[1])
      count += 1

  print(aux, count)

  if aux[count][1] >= mx[2][0]:
      aux[count][1] = mx[2][1]
  else:
      aux.append(mx[2])
      count += 1

  print(aux, count)

  if aux[count][1] >= mx[3][0]:
      print("if")
      aux[count][1] = mx[3][1]
  else:
      print("else")
      aux.append(mx[3])
      count += 1

  print(aux, count)'''