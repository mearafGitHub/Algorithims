def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)-1
    b = a[: mid]
    c = a[mid: n-1]
    b.append(a[n-1])
    b.extend(c[::-1])
    a = b
    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

def findZigZagSequence2(a, n):
    a.sort()
    mid = int((n + 1)/2)-1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return