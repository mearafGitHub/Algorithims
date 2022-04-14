import heapq


def kth_smallest_task(task):
    result =[]
    heapq.heapify(task)
    kth = []
    for _ in range(len(task)):
        pass
    for t in range(3):
        result.append(heapq.heappop(task))
    return result



task = [(10, 'clean'), (5, 'do map'), (8, 'excel'), (7, 'queue'), (2, 'tools'), (4, 'make')]
print(kth_smallest_task(task))