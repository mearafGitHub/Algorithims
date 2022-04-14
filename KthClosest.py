from heapq import *

def kth_closest(points, k):
    store = []
    kth = []
    for x, y in points:
        d = (x ** 2) + (y ** 2)
        heappush(store, [d, x, y])

    for i in range(k):
        kth.append(store[i][1:])

    return kth


print(kth_closest([[2,4], [7,1], [0,9], [3,2]], 0))
