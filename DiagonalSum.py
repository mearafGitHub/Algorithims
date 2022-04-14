Diagonal
sum(Easy)


def digonalSum(matrix):
    left_right_sum = 0
    right_left_sum = 0
    absolute_dif = 0
    r, c = 0, 0
    j = len(matrix[0]) - 1

    while r < len(matrix) and c < len(matrix[0]) and j >= 0:
        print('while...', matrix[r][c], matrix[r][j])
        left_right_sum += matrix[r][c]
        right_left_sum += matrix[r][j]
        r += 1
        c += 1
        j -= 1

    absolute_dif = abs(left_right_sum - right_left_sum)
    return (absolute_dif, left_right_sum, right_left_sum)


print(digonalSum([[1, 2, 3], [4, 5, 6], [14, 8, 9]]))
