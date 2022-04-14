def medianTwoSortedArrays(X, Y):
    if len(X) > len(Y):
        medianTwoSortedArrays(Y, X)
    x = len(X)
    y = len(Y)
    start = 0
    end = len(X)
    totalLen = len(X) + len(Y)
    median = 0
    while start <= end:
        px = (start + end) // 2
        py = ((totalLen + 1) // 2) - px

        xMinRight = X[px] if px < x else float('inf')
        yMinRight = Y[py] if py < y else float('inf')

        xMaxLeft = X[px - 1] if px > 0 else float('-inf')
        yMaxLeft = Y[py - 1] if py > 0 else float('-inf')
        # print(
        #     'start:', start,
        #     '\nend:', end,
        #     '\npx:', px,
        #     '\npy:', py,
        #     '\nxMinRight:', xMinRight,
        #     '\nyMinRight:', yMinRight,
        #     '\nxMaxLeft:', xMaxLeft,
        #     '\nyMaxLeft:', yMaxLeft
        # )
        if xMaxLeft <= yMinRight and yMaxLeft <= xMinRight:
            if totalLen % 2 == 0:
                num1 = max(xMaxLeft, yMaxLeft)
                mun2 = min(xMinRight, yMinRight)
                median = float((num1 + mun2) / 2)
                print('even median: ', median)
                return median
            else:
                median = max(xMaxLeft, yMaxLeft)
                print('odd median: ', median)
                return median
        elif xMaxLeft > yMinRight:
            end = px - 1
        else:
            start = px + 1

    return median


a = [1, 2, 3, 100, 201]
b = [4, 5, 6, 7, 56, 78]
print('Median: ', medianTwoSortedArrays(a, b))

