'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

def spiralOrderClockWise(matrix):
    rows, cols = len(matrix), len(matrix[0])
    x, y, dx, dy = 0, 0, 0, 1
    res = []

    for _ in range(rows * cols):
        res.append(matrix[x][y])
        matrix[x][y] = "."

        if not 0 <= x + dx < rows or not 0 <= y + dy < cols or matrix[x+dx][y+dy] == ".":
            dx, dy = dy, -dx
            
        x += dx
        y += dy
        
    return res

#  --------------------------------------------

def spiralOrderAntiClockwise(matrix):
    rows, cols = len(matrix), len(matrix[0])
    x, y, dx, dy = 0, 0, 1, 0
    res = []

    for _ in range(rows * cols):
        res.append(matrix[x][y])
        matrix[x][y] = "."

        if not 0 <= x + dx < rows or not 0 <= y + dy < cols or matrix[x+dx][y+dy] == ".":
            dx, dy = -dy, dx
            
        x += dx
        y += dy
        
    return res

#  --------------------------------------------

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
result1 = spiralOrderClockWise(matrix1)
print(result1)

matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
result2 = spiralOrderAntiClockwise(matrix2)
print(result2)
