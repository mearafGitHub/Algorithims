#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    print('n  ', n, '  m  ', m)
    if n == 1:
        return 1

    if n == 0 or m == 0:
        return 0

    if m == 1:
        return 2

    if m > 1 and n >= 2:
        T1, T2 = m, m
        turn = 1
        while T1 > 0 or T2 > 0:
            # y = int(input().split())
            y = math.Random()
            if y >= 1:
                if turn == 1:
                    if T1 % y == 0:
                        T1 - y
                        turn = 2
                    else:
                        return 2

                if turn == 2:
                    if T2 % y == 0:
                        T2 - y
                        turn = 1
                    else:
                        return 1


def towerBreakers2(n,m):
    if m == 1:
        print(2)
    else:
        if n % 2 == 1:
            print(1)
        else:
            print(2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
