from heapq import *
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
    # store the greater ones in the 'upper' P. queue
    if curNumber >= middle:
        heappush(upper, curNumber)
    # store the smaller ones in the 'under' P. queue
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


# +++++++++++++++++++++++++++++++++++++++++++++++
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
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


def sort_(r, x):
    a = r
    i = 0
    while True:
        if i > len(a):
            return

        if i == len(a):
            a.append(x)
            return a

        if len(a) > 0:
            if x < a[i]:
                temp = [x]
                temp.extend(a)
                a = temp
                return a

        if x < a[i] and 1 < len(a):
            temp = a[:i]
            temp.append(x)
            temp.extend(a[i - 1:])
            a = temp
            return a

        if i + 1 < len(a):
            if x > a[i] and x < a[i + 1]:
                temp = a[:i + 1]
                print("temp", temp)
                temp.append(x)
                print('temp', temp)
                temp.extend(a[i + 1:])
                print('temp', temp)
                a = temp
                return a

        if x > a[i] and i + 1 > len(a):
            temp.extend([x])
            return a

        else:
            i += 1

    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a = sort_(a, a_item)
        # print("a =>  ",a)
        median = runningMedian(a)
        print(median)

        fptr.write(str(median))
        fptr.write('\n')

    fptr.close()
