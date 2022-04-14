def firstNonRepeating(arr):
    count = {}
    for a in arr:
        if a in count:
            count[a] = 1
        else:
            count[a] = 0
    for c in arr:
        if count[c] == 0:
            return c
    return '_'


print(firstNonRepeating('abababamhagshf'))
