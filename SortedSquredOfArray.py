def sortedSquared(arr):
    out = [0 for _ in range(len(arr))]

    l = 0
    r = len(arr) - 1

    for i in range(len(arr) - 1, -1, -1):
        left = arr[l] ** 2
        right = arr[r] ** 2
        if left >= right:
            out[i] = left
            l += 1
        else:
            out[i] = right
            r -= 1

    return out


print(sortedSquared([-3, 2, 3, 5]))
