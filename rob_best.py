"""
can't rob neighbour houses, but skip by one
choose the best pattern to rob to gain maximum robbery
"""

def rob(houses):
    r1, r2 = 0, 0
    for h in houses:
        temp = max(h+r1, r2)
        r1 = r2
        r2 = temp

    return r2


print(rob([2, 10, 5, 3, 1, 7,4]))
