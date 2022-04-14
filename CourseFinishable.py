def dfsCourseSchedule(course, pre, visited):
    if pre[course] == []:
        return True

    if course in visited:
        return False

    visited[course] = course
    for crs in pre[course]:
        finishable = dfsCourseSchedule(crs, pre, visited)
        for c in crs:
            return dfsCourseSchedule(c, pre, visited)


def courseFinishable(n, dagEdges):
    pre = {x: [] for x in range(n)}
    print(pre)
    visited = {}
    for pair in dagEdges:
        pre[pair[0]].append(pair[1])
    for c in range(n):
        if dfsCourseSchedule(c, pre, visited):
            return True
    print(pre)
    return False


pq = [[0, 1], [0, 2], [1, 3], [3, 4], [1, 4]]
print(courseFinishable(5, pq))
