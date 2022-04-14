#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

import os
from heapq import *


def running_median():

    under = []
    upper = []
    N = int(input())
    for _ in range(N):
        curNumber = int(input())
        if (len(upper) == 0):
            upper.append(curNumber)
            print(curNumber)
            continue
        middle = upper[0]
        # store the greater ones in the 'upper' P.queue
        if curNumber >= middle:
            heappush(upper, curNumber)
        # store the smaller ones in the 'under' P.queue
        else:
            heappush(under, -curNumber)
        # balancing the tree / priority queue
        if len(under) >= len(upper):
            heappush(upper, -heappop(under))
        if len(upper) >= len(under) + 2:
            heappush(under, -heappop(upper))
        if (len(upper) + len(under)) % 2 == 1:
            print(float(upper[0]))
        else:
            print((float(upper[0]) + -under[0])/2)

def runningMedianSmall(a):
    median = 0.0
    if len(a) == 1:
        median = float(a[0])
        return median

    if len(a) == 2:
        median = float(a[0] + a[1]) / 2
        return median

    if len(a) > 2:
        i = len(a) // 2
        if len(a) % 2 == 0:
            median = float(a[i - 1] + a[i]) / 2
            return float(median)

        elif len(a) % 2 != 0:
            i = len(a) // 2
            median = float(a[i])
            return median

    return median


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a_count = int(input().strip())
    a = []
    for _ in range(a_count):
        a_item = int(input().strip())
        median = runningMedian(a)
        print(median)

        fptr.write(str(median))
        fptr.write('\n')

    fptr.close()
