def max_sub(nums):
    maxsum = nums[0]
    curr = 0

    for n in nums:
        if curr < 0:
            curr = 0
        curr += n
        maxsum = max(maxsum, curr)
    return maxsum


print(max_sub([1, -2, 3, 4, -1, 5, 8]))

print(max_sub([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
