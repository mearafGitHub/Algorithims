def courseFinishableII(course, pre, visited, order):
    if course in visited:
        return (False, order)

    order.append(course)
    visited[course] = course

    if pre[course] == []:
        return (True, order)

    for crs in pre[course]:
        finishable = courseFinishableII(crs, pre, visited, order)
        if not finishable[0]:
            return (False, finishable[1])
    pre[course] = []
    return (True, order)


pq = [[0,1], [0,2], [1,3], [3,4], [1,4]]
print(courseFinishableII(5, pq))
