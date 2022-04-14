def min_rotated(nums):
    # return min(nums)  ==> O(n) time
    smallest = nums[0]
    l, r = 0, len(nums)-1
    while l < r:
        if nums[l] < nums[r]:
            smallest = min(smallest, nums[l])
            break
        mid = (l+r)//2
        smallest = min(smallest, nums[mid])
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    return smallest

print(min_rotated([5,6,7,0,2,3,4]))
