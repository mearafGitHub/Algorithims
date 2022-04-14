"""
return the indices of the tow elements that sums to a given target number in an array
"""

def two_sum_ii(nums, n):
    i = 0
    j = len(nums)

    if nums[i] == n:
        return [i]
    if nums[j] == n:
        return [j]

    while i < j:
        if nums[i] + nums[j] > n:
            j -= 1
        if nums[i] + nums[j] < n:
            i += 1
        else:
            # if indexes are based on one then add 1 to each of them. else, don't.
            return [i+1, j+1]
    return []
