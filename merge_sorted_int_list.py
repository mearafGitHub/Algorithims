"""
m is number of elements in first and n in second
first has space ready to accommodate all elements in second, currently filled with zeros
"""
# two pointer solution m pointing first from the last
# n pointing second from the last
# to merging from the last index


def merge(first, m, second, n):
    last = (m+n) - 1

    while m > 0 and n > 0:
        if first[m-1] > second[n-1]:
            first[last] = first[m-1]
            m -= 1
        else:
            first[last] = second[n-1]
            n -= 1

        last -= 1

    #
    while n > 0:
       first[last] = second[n]
       n, last = n-1, last-1
