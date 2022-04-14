"""
product of items except self and return the corresponding res in output array
time should be => O(n)
"""


def prod_except_self(nums):
    output = [1] * len(nums)
    pre, post = 1, 1
    for i in range(len(nums)):
        output[i] = pre
        pre *= nums[i]

    for j in range(len(nums)-1, -1, -1):
        output[j] *= post
        post *= nums[j]

    return output

print(prod_except_self([11,12,13,14]))

