def largest_seq(seq):
    nums_map = {n: 0 for n in seq}
    left, right = 0, 0

    for n in seq:
        if nums_map[n] == 0:
            left_ = n - 1
            right_ = n + 1
            while left_ in nums_map:
                nums_map[left_] = 1
                left_ -= 1
            left_ += 1
            while right_ in nums_map:
                nums_map[right_] = 1
                right_ += 1
            right_ -= 1

            if (right - left) <= (right_ - left_):  # if the range/size of the previous sub array is small
                right, left = right_, left_    # then replace it by the current one to get the largest sequence

    return [left, right]  # the smallest num and the largest num in the sequential numbers

print(largest_seq([10, 24, 5, 9, 1, 0, 3, 7, 6, 2, 20, 8, 4, 21, 25, 23, 22]))
print(largest_seq([10, 24, 5, 1, 0, 2, 20, 8, 4, 21, 25, 23, 22]))
