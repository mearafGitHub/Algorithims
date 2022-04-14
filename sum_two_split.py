
def sum(arr):
    p1, p2 = '', ''
    mid = 0
    lng = len(arr)
    if lng % 2 == 0:
        mid = (lng//2)
        for i in range(lng-mid, lng):
            p2 += arr[i]
        for j in range(mid-1, -1, -1):
            p1 += arr[j]
        return int(p2)+int(p1)
    else:
        mid = (lng // 2)
        for i in range(mid+1, lng):
            p2 += arr[i]
        for j in range(mid, -1, -1):
            p1 += arr[j]
        return (int(p2) + int(p1))

print(sum('4325'))
