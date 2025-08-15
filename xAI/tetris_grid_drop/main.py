def tetris_grid_drop(mx_grid, mx_piece):
    idx = 0

    print(mx_grid, mx_piece)

    piece_width = 0
    count = 0

    for x in range(0, len(mx_piece)):
        for y in range(0, len(mx_piece)):
            if mx_piece[x][y] == 1:
                count += 1

        if count > piece_width:
            piece_width = count
            count = 0

    print(piece_width)


    return idx

print(tetris_grid_drop([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0]
], [
    [0, 1, 0],
    [1, 1, 1],
    [0, 0, 0]
]))