def binarySearch(data, find):
    mid = len(data) // 2
    l, r = 0, len(data)
    if not data:
        return False
    if find == data[mid]:
        print('data[mid]:  ', data[mid], find)
        return True
    elif find > data[mid]:
        l = mid + 1
        binarySearch(data[l:r], find)
    elif find < data[mid]:
        r = mid
        binarySearch(data[l:r], find)


data = [2, 4, 6, 8, 9, 10, 12, 34]
find = 100

print(binarySearch(data, find))
