
def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    matrix = [[0 for i in range(n + 2)] for j in range(n + 2)]
    print(matrix)

    direction = 0
    x = 1
    y = 1
    # matrix[1][1] = 1
    number = 0
    while True:
        number = number + 1
        matrix[x][y] = number
        print(x, y, '->', matrix[x][y])
        # print(matrix)
        if matrix[x+1][y] != 0 and matrix[x][y+1] != 0 and matrix[x-1][y] != 0 and matrix[x][y-1] != 0:
            print('stop')
            break
        # if not ((direction == 0) and (x+1 < n) and (matrix[x+1][y] == 0)) or\
        #    not ((direction == 1) and (y+1 < n) and (matrix[x][y+1] == 0)) or\
        #    not ((direction == 2) and (x-1 > 0) and (matrix[x-1][y] == 0)) or\
        #    not ((direction == 3) and (y-1 > 0) and (matrix[x][y-1] == 0)):
        #         print('change direction')
        #         direction = (direction + 1) % 4

        if (direction == 0 and not((y+1 < n+1) and (matrix[x][y+1] == 0))) or \
            (direction == 1 and not ((x+1 < n+1) and (matrix[x+1][y] == 0))) or \
             (direction == 2 and not ((y-1 > 0) and (matrix[x][y-1] == 0))) or \
              (direction == 3 and not ((x-1 > 0) and (matrix[x-1][y] == 0))):
                    print('change direction')
                    direction = (direction + 1) % 4
        if direction == 0:
            print('direct ', direction)
            y = y+1
        elif direction == 1:
            print('direct ', direction)
            x = x+1
        elif direction == 2:
            print('direct ', direction)
            y = y-1
        elif direction == 3:
            print('direct ', direction)
            x = x-1
    result = [matrix[i][1:n+1:] for i in range(1, n+1)]

    return result
# print(generateMatrix(8))
def printmatrix(a):
    print("Printing matrix")
    for x in a:
        print(x)
printmatrix(generateMatrix(2))
# printmatrix(generateMatrix(4))
