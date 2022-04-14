def sumPair(data, s):
    if not data:
        return False

    differences = {}
    for d in data:
        if d < s or d > s:
            dif = s - d
            if dif in differences:
                return (True, [dif, d])
        differences[dif] = d

        # O(n) time and space (worest case)
    return False


print('sumPair:  ', sumPair([1, 2, 4, 6, 4], 8))


def sumList(data, s):
    result = []
    sub_res = []
    latest = 0
    for i in data:
        if i == s:
            sub_res = []
            sub_res.append(i)
            result.append(sub_res)
            latest = 0
            sub_res = []
        if latest + i < s:
            latest += i
            sub_res.append(i)
        if latest + i == s:
            sub_res.append(i)
            result.append(sub_res)
            sub_res = []
            latest = 0
        if latest + i > s:
            sub_res = []
            latest = 0
    # O(n) time and space complexity (worest case)
    return result


print('sumList"  ', sumList([1, 2, 4, 6, 4], 8))


def sumPairSortedlist(data, s):
    pair = []
    l, r = 0, len(data) - 1
    while l < r:
        if data[l] + data[r] == s:
            pair.append([(l, data[l]), (r, data[r])])
            l += 1
            r -= 1
        if data[l] + data[r] > s:
            r -= 1
        if data[l] + data[r] < s:
            l += 1
    # O(n) time and space(worst case)
    return pair


print('sumPairSortedlist:   ', sumPairSortedlist([1, 2, 3, 4, 5, 6], 8))