def longestConsq(nums):
    longest = 0
    myset = set(nums)
    # nums.sort()
    curLong = 0
    for n in nums:
        if n - 1 in myset:
            curLong += 1
        longest = max(longest, curLong)
    return longest


print(longestConsq([100, 4, 200, 1, 3, 2, 5]))
