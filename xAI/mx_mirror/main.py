def mx_mirror(mx):
    '''x = 0
    y = 0

    temp = mx[x][y]
    mx[x][y] = mx[y][x]
    mx[y][x] = temp

    x = 0
    y = 1

    temp = mx[x][y]
    mx[x][y] = mx[y][x]
    mx[y][x] = temp

    x = 0
    y = 2

    temp = mx[x][y]
    mx[x][y] = mx[y][x]
    mx[y][x] = temp

    x = 1
    y = 1

    temp = mx[x][y]
    mx[x][y] = mx[y][x]
    mx[y][x] = temp

    x = 1
    y = 2

    temp = mx[x][y]
    mx[x][y] = mx[y][x]
    mx[y][x] = temp'''

    print(len(mx[0]))
    for x in range(0, len(mx[0])):
        for y in range(x, len(mx[0])):
            temp = mx[x][y]
            mx[x][y] = mx[y][x]
            mx[y][x] = temp

    return mx

print(mx_mirror([
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]))

print(mx_mirror([
 [1, 4],
 [9, 8],
 [2, 5]
]))