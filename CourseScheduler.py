def courseScheduler(n, dagEdges):
    pre = {x: [] for x in range(n)}  # O(V)
    print(pre)
    visited = {}
    order = []
    for pair in dagEdges:   # O(E)
        pre[pair[0]].append(pair[1])
    for c in range(n):   # O(V)
        finished = dfsCourseSchedule(c, pre, visited, order) # O(m) -> O(Vm)
        if finished[0]:
            topologicalOrder = finished[1][::-1]
            return (True, topologicalOrder)
    print(pre)
    return False
# O(V + Vm + E) Vm = V + E  -> O(2(V+E)) -> O(V+E) Time and Space
pq = [[0,1], [0,2], [1,3], [3,4], [1,4]]
print(courseScheduler(5, pq))
