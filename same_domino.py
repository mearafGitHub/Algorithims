def same_domino_swap(tops, bottoms):
    t = {}
    b = {}
    cmnT = [0, 0]
    cmnB = [0, 0]
    result = -1
    for i in range(len(tops)):
        t[tops[i]] = t.get(tops[i], 0) + 1
        b[bottoms[i]] = b.get(bottoms[i], 0) + 1
    # counting the most commun values
    for key, value in t.items():
        if cmnT[1] < value:
            cmnT = [key, value]
    for key, value in b.items():
        if cmnB[1] < value:
            cmnB = [key, value]
    if cmnT[0] == cmnB[0]:
        result = len(tops) - max(cmnB[1], cmnT[1])
        return result

    return result


print(same_domino_swap(
    [3, 2, 4, 2, 2],
    [5, 7, 3, 2, 2]))

"""
Given two dominoes top and bottom,
how many swaps must happen to make ether of the dominos the same number?
if there is no possibility the return -1.
"""