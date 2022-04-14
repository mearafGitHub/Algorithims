from heapq import heapify, heappush, heappop

minheap = []
maxheap = []
heapify(minheap)
heapify(maxheap)


class RealtimeMedian:

    def balanceHeap(self):
        lenMin = len(minheap) if minheap else 0
        lenMax = len(maxheap) if maxheap else 0

        if lenMax > lenMin:
            if lenMax - lenMin > 1:
                x = heappop(maxheap)
                heappush(minheap, -1 * x)
        elif lenMin > lenMax:
            if lenMin - lenMax > 1:
                x = -1 * heappop(minheap)
                heappush(maxheap, x)

    def addNum(self, k):
        if maxheap and minheap:
            if k <= maxheap[0]:
                heappush(maxheap, k)
            else:
                heappush(minheap, -1 * k)
        elif maxheap:
            if k <= maxheap[0]:
                heappush(maxheap, k)
            else:
                heappush(minheap, k)
        elif minheap:
            if -1 * k >= minheap[0]:
                x = heappop(minheap)
                heappush(minheap, -1 * k)
                heappush(maxheap, -1 * x)
            else:
                heappush(maxheap, k)
        else:
            heappush(minheap, -1 * k)

        self.balanceHeap()

    def runningMedian(self, k):
        self.addNum(k)
        median = -1
        if minheap and maxheap:
            minLen = len(minheap)
            maxLen = len(maxheap)
            if maxLen > minLen:
                return heappop(maxheap)
            elif maxLen == minLen:
                a = -1 * heappop(minheap)
                b = heappop(maxheap)
                return float(a + b) / 2
            elif maxLen < minheap:
                return -1 * heappop(minheap)
        elif maxheap:
            return maxheap[0]
        else:
            return -1 * minheap[0]

        return median


def main(array):
    median = 0
    for a in array:
        med = RealtimeMedian()
        median = med.runningMedian(a)
        print(median)


main([10, 4, 8, 2, 6, 5, 2, 4])
