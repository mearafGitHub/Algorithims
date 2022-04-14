def can_sum(target, nums, memo={}):
    if target in memo:
        return True
    if target == 0:
        return True
    if target < 0:
        return False
    dif = 0
    for n in nums:
        if n == dif and dif > 0:
            memo[n] = n
            return True
        dif = target - n
        print("Iteration:  ", n, dif)
        if dif == 0 or dif in memo:
            return True
        else:
            memo[dif] = False

    return False


print(can_sum(110, [7,5,6,4]))

# Time: O(n)
# Space: O(n)

