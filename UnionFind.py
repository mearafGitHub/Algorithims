data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Quick Find's Union function is { O(n2) worste case, not efficient}
def isConnected(p, q):  # union find operation
    return data[p] == data[q]


def union(p, q):
    for i in range(len(data)):
        if data[i] == data[p]:
            data[i] = data[q]
    return data


# print(union(1,2))
# print(union(3,2))
# print(isConnected(1,2))

# Quick Union
def root(i):
    while not (i == data[i]) and i < len(data) - 1:  # while malfunctions
        data[i] = data[data[i]]
        i = data[i]
    return i


def findQuickUnion(p, q):
    pr = root(p)
    qr = root(q)
    # print('findQuickUnion:  ',pr, '  ', qr)
    return pr == qr


def quickUnion(p, q):
    i = root(p)
    j = root(q)

    data[p] = j
    return data


# print(quickUnion(1,2))
# print(quickUnion(4,8))
# print(findQuickUnion(2,8))

# Weighted Quick union path compression Algorthm runs on
# O(N = M + N log * N) time fo Weighted union
# O(p + q) for find
# Weighted improves scalability and efficiency radically, it uses the same find function and
# a modified root function in quick union algo
sz = [1 for _ in range(len(data))]


def weightedUnion(p, q):
    i = root(p)
    j = root(q)
    # print('Root p: ', i, '   Root q: ', j)
    if i == j:
        return data

    if sz[i] < sz[j]:
        data[i] = j
        sz[j] += sz[i]
    else:
        data[j] = i
        sz[i] += sz[j]

    return data


print(weightedUnion(1, 2))
print(weightedUnion(1, 4))
print(sz[1])
print(findQuickUnion(2, 4))

