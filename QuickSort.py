def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[low] <= pivot:
            low = low + 1
        while low <= high and array[high] >= pivot:
            high = high - 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quick_sort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)

    quick_sort(array, start, p)
    quick_sort(array, p + 1, end)


arr = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
a = [1, 0, 2, 1, 1, 0, 2, 0, 2]
b = [2, 4, 5]
quick_sort(b, 0, len(b) - 1)
print(b)
