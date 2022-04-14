from collections import Counter, defaultdict, OrderedDict
import heapq


def topKFrequent(nums, k):
    count = Counter(nums)
    print(count)
    return [i for i, _ in count.most_common()]


def K_most_frequent(nums, k):
    map = defaultdict(list)
    freq = [[] for _ in range(len(nums)+1)]
    for n in nums:
        map[n] = 1 + map.get(n, 0)
    for n, v in map.items():
        freq[v].append(n)
    res = []
    for i in range(len(freq)-1, -1, -1):
        for j in freq[i]:
            res.append(j)

    return res[:: -1]


def k_top(nums, k):
    freq = OrderedDict()
    k_ = []
    for n in nums:  # O(n)
        freq[n] = 1+freq.get(n, 0)

    freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[-1])}  # O(nlogn)  we need the top ones

    keys = list(freq.keys())   # O(n)

    for i in range(len(list(freq.values())) - 1, -1, -1):    # O(n.k)
        if k > 0:
            k_.append(keys[i])
            k -= 1
        else:
            break
    return k_
# time:  O(nlogn) + O(2n) + O(n.k)  ->
# memory:  O(n) + O(k)
print(k_top([1,13,23,3,1,1,2,2,1,5,5,5,5,3,3,3,5,3,3,3,3,3], 2))