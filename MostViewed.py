# sorted(List_name, key=lambda x: x[1])
# List of LIST and TUPLE List_name.sort(key=lambda x: x[1])

def mostViewed(v, k):
    res = []
    v.sort(key=lambda x: x[1])  # O(n log n)
    for i in range(k):
        res.append(v[i])
    return res


print(mostViewed([('abc', 19), ('ddef', 15), ('xyz', 100), ('ghi', 10), ('abc', 12)], 3))  # O(n log n + k)
