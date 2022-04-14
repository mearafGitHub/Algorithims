def grap(h, n):
    # hey-stack h, needle n
    word = ''
    indexes = []
    if (len(h) < len(n)):
        error = "needle is bigger than the hey-stack :("
        return error

    if h == '':
        error = "no match for empty string."
        return error
    if n == '':
        return indexes
    for i in range(0, len(h)):
        for j in range(0, len(n)):
            #  compare chars
            if (i + j) < len(h):
                if h[i + j] == n[j]:
                    word += h[i + j]
        if (word == n):
            indexes.append(i)
            word = ''
        else:
            word = ''
    return indexes


x = grap('aaabcdddejfdjbabcuihd',
         'fd')

print(x)
# time = O(n*m)
# space = O(i) ,  i = number of indexes