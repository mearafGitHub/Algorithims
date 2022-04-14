#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(st, k):
    # Write your code here
    # to keep the last letter comming to the front
    small = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    big = [chr(C) for C in range(ord('A'), ord('Z') + 1)]
    cipher = ""
    for c in st:
        if c in small:
            cipher += small[(small.index(c) + k) % 26]
        elif c in big:
            cipher += big[(big.index(c) + k) % 26]
        else:
            cipher += c

    return cipher


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
