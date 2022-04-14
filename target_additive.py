"""
from a given array, find two elements that adds up to a given tagert value t
explanation:
if a[i] + a[j] = t then return (i, j)
"""

def two_sum(arr, t):
    # copy ech elements to a hash map and check if we find the elements as we do the copying
    table = {}
    for i in range(len(arr)):
        diff = t-arr[i]
        if diff in table:
            return (i, table[diff])

        table[arr[i]] = i

    return None

print(two_sum([1,5,3,6,4,8], 11))