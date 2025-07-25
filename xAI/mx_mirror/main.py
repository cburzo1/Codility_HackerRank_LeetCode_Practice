'''
MY ATTEMPT:

def mx_mirror(mx):

    if len(mx) == len(mx[0]):
        for x in range(0, len(mx[0])):
            for y in range(x, len(mx[0])):
                temp = mx[x][y]
                mx[x][y] = mx[y][x]
                mx[y][x] = temp
    else:
        mxa = [[0 for _ in range(len(mx))] for _ in range(len(mx[0]))]

        for x in range(0, len(mx[0])):
            for y in range(0, len(mx)):
                mxa[x][y] = mx[y][x]

        mx = mxa

    return mx
'''

def mx_mirror(mx):
    rows = len(mx)
    cols = len(mx[0])

    if rows == cols:
        # In-place transpose for square matrix
        for x in range(cols):
            for y in range(x, cols):
                mx[x][y], mx[y][x] = mx[y][x], mx[x][y]
        return mx
    else:
        # New transposed matrix for non-square
        mxa = [[0 for _ in range(rows)] for _ in range(cols)]
        for x in range(cols):
            for y in range(rows):
                mxa[x][y] = mx[y][x]
        return mxa

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

print(mx_mirror([
 [1, 4, 2],
 [9, 8, 7]
]))

'''
MAIN TAKEAWAYS:

- traverse a list with a nested for loop and access their x and y
- get the length and width of a matrix if not given
- understand what a transpose matrix is
- memorize empty 2d list creation
'''