def mostFreq(nums, k):
    counter = {}

    for n in nums:
        counter[n] = counter.get(n, 0) + 1

    bucket = [[] for _ in range(len(counter.keys())-1)]

    for n in nums:
        bucket[counter[n]] = n

    return bucket[len(bucket)-k: len(bucket)]


print('Time: O(n) where n = len(nums), space: O(2n)->worst case')
print(mostFreq([1,2,6,2,3,1,5,5,5], 2))

