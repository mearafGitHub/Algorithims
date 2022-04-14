def in_rotated_sorted(nums, t):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == t:
            return mid
        if nums[mid] >= nums[l]:
            if t > nums[mid] or t < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if t < nums[mid] or t > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1


print(in_rotated_sorted([5, 6, 7, 0, 2, 3, 4], 7))
