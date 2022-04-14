def min_no_ops(nums, k):
    ops = 0
    i = 0
    if not nums:
        return 0
    while i+k < len(nums):
        if nums[i] > nums[i+k]:
            print(nums[i])
            nums[i], nums[i+k] = nums[i+k], nums[i]
            ops += 1
        i += 1
    print(nums)
    return ops

print(min_no_ops([1,2,0,1,2],3))