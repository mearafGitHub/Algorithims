
def merge(array, left_index, right_index, middle):
    left_copy = array[left_index:middle+1]
    right_copy = array[middle+1:right_index+1]

    i = 0
    j = 0
    k = i

    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            array[k] = left_copy[i]
            i += 1
        else:
            array[k] = right_copy[j]
            j += 1

        k += 1

    while i < len(left_copy):
        array[k] = left_copy[i]
        i += 1
        k += 1

    while j < len(right_copy):
        array[k] = right_copy[j]
        j += 1
        k += 1


def mergeM(array, left_index, right_index, middle):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def merge_sort(array, l, r):
    if l >= r:
        return
    middle = (l + r) // 2
    merge_sort(array, l, middle)
    merge_sort(array, middle+1, r)
    mergeM(array, l, r, middle)


data = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
merge_sort(data, 0, len(data) - 1)
print(data)

print('Expected:  ',
      [4, 5, 8, 9, 16, 22, 26, 29, 31, 33, 37, 42, 47, 48, 49])
