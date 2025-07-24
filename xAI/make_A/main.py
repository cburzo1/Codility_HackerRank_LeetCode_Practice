def make_A(x, y):
    Amx = [[0 for _ in range(x)] for _ in range(y)]

    mid = y//2

    # align mid
    for i in range(0, x):
        Amx[mid][i] = 1

    for i in range(1, mid):
        Amx[mid - i][i] = 1
        Amx[mid - i][(x - i) - 1] = 1

    Amx[0][mid] = 1

    for i in range(0, mid + 1):
        Amx[mid + i][0] = 1

    for i in range(0, mid + 1):
        Amx[mid + i][x - 1] = 1

    return Amx

print(make_A(5, 5))