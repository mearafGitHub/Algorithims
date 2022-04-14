def floyd_warshall(V, E, W):

    distance = {(x, x): 0 for x in V}
    for u, v in E:
        distance[(u, v)] = W[(u, v)]
    n = len(V) + 1
    for k in V:
        for i in V:
            for j in V:
                if (i, j) in distance and (k, j) in distance and (i, k) in distance:
                    if distance[(i, j)] > distance[(k, j)] + distance[(i, k)]:
                        distance[(i, j)] = distance[(k, j)] + distance[(i, k)]
                elif (k, j) not in distance:
                    distance[(k, j)] = 0
                elif (i, k) not in distance:
                    distance[(i, k)] = 0
                elif (i, j) not in distance:
                    distance[(i, j)] = distance[(k, j)] + distance[(i, k)]
    return distance

w = {(2,9): 10, (1,4): 5, (1,9): 3, (2,4): 4}

print('Made for directed graph: O(V**3) ')
print(floyd_warshall([2, 9, 1, 4], [(2, 9), (1, 4), (1, 9), (2, 4)], w))
