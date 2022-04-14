
"""
Floyd's algo to find dupplicate in a linked list => detecting a cycle in a linked list
This a linked list problem.

nums contain the nums from 1-n but have n+1 element. Only one element is a dupliacte.
"""

def find_duplicate(nums):
    fast, slow = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow_2 = 0
    while True:
        slow = nums[slow]
        slow_2 = nums[slow_2]
        if slow == slow_2:
            return slow
        