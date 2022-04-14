# O(n) time and O(1) space using in-space swap

def rotateImage(matrix):
    # 90 degree clock wise
    n = len(matrix)
    if len(matrix[0]) != n:
        return "Invalid Input"

    # swap columns
    for i in range(n - 1):
        for j in range(len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # swap the firs and end elements ofthe result off first step to make 90 degree
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][0], matrix[i][n - 1] = matrix[i][n - 1], matrix[i][0]

    return matrix


print(rotateImage([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
