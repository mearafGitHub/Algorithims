"""
return the maximum value of a sum in sub arrays in a give array of both negative and positive integers
"""


def max_sum_subarray(arr):
    if not arr:
        return 0

    max_sum = arr[0]
    cur_max = 0

    for i in arr:
        if i < 0:
            cur_max = 0
        cur_max += i
        max_sum = max(max_sum, cur_max)

    return max_sum
