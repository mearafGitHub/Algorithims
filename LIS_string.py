#  the solution for longest common pattern in two given strings
#
def LIS_str(text1, text2):
    matrix = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
    print(len(text1), '  ', len(text2), " ", matrix[5][3])

    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]:
                matrix[i][j] = 1 + matrix[i+1][j+1]
            else:
                matrix[i][j] = max(matrix[i][j + 1], matrix[i + 1][j])

    return matrix[0][0]

print(LIS_str('abcde', 'ace'))
