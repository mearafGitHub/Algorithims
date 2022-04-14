import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        kth = []

        for x, y in points:
            d = math.sqrt(x ** 2 + y ** 2)
            res.append([d, [x, y]])

        res.sort(key=lambda item: item[0])
        print(res)

        for i in range(0, k):
            dist, point = res[i]
            print(point)
            kth.append(point)

        return kth
