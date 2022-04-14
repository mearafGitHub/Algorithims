def max_prod(nums):
    res = max(nums)
    curr_max, curr_min = 1, 1
    for n in nums:
        if n < 0:
            curr_max, curr_min = 1, 1
        temp = n * curr_max
        curr_max = max(curr_max * n, curr_min * n, n)
        curr_min = min(temp, n, curr_min)
        res = max(res, curr_max)
    return res

print(max_prod([5,-2, 3,4, 0, 1, 2]))