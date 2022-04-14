def twoSum(a, b, v):
    if len(b) < len(a):
        twoSum(b, a)

    i = 0
    j = 0
    A = {}
    B = {}
    while i < len(a) and j < len(b):
        print(i, j)
        if a[i] != v and b[i] != v:
            if a[i] not in A:
                A[a[i]] = a[i]
            if b[i] not in B:
                B[b[i]] = b[j]

            da = v - a[i]
            db = v - b[j]

            if da in B:
                return [a[i], B[da]]
            if db in A:
                return [b[j], A[db]]

        if i < len(a):
            i += 1
        j += 1

    return 0


print(twoSum([2, 4, 8, 1], [5, 7, 1, 3, 4], 8))