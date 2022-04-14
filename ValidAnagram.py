def valid(s1, s2):
    map1 = {}
    map2 = {}
    if len(s1) != len(s2):
        return False

    i = 0
    while i < len(s1):
        map1[s1[i]] = map1.get(s1[i], 0) + 1
        map2[s2[i]] = map2.get(s2[i], 0) + 1
        i += 1

    for c in s1:
        if map1[c] != map2.get(c, 0):
            return False

    return True

print(valid('come', 'more'))
