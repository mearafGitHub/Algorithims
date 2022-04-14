import heapq


def longest_happy(a, b, c):
    my_heap = []
    result = ''
    for n, c in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
        if n < 0:
            heapq.heappush(my_heap, (n, c))
    print(my_heap)

    while my_heap:
        n_, c_ = heapq.heappop(my_heap)
        print("n_, c_    ", n_, c_, '   result  ', result)
        if len(result) > 1 and result[-1] == result[-2] == c_:
            if not my_heap:
                break
            n__, c__ = heapq.heappop(my_heap)
            print('n__, c__    ', n__, c__)
            result += c__
            n__ += 1
            if n__ != 0:
                heapq.heappush(my_heap, (n__, c__))
        else:
            result += c_
            n_ += 1
        if n_ != 0:
            heapq.heappush(my_heap, (n_, c_))

    return result