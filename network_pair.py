import heapq

def always_on():
    c = [[1,2], [1,3], [2,4],[3,4],[3,6],[6,7], [4,5]]
    map = {}
    for a, b in c:
        if a not in map:
            map[a] = [1]
            map[a].append(b)
        elif map[a]:
            map[a][0] += 1
            if b not in map[a]:
                map[a].append(b)
        if b not in map:
            map[b] = [1]
            map[b].append(a)
        elif map[b]:
            map[b][0] += 1
            if a not in map[b][1:]:
                map[b].append(a)


    net = list(map.items())
    heapq.heapify(net)
    print(net)
    # print(map)
    must = []
    i = 0
    for s, r in net:
        # print(s, r)
        if 1 == r[0]:
            must.append(r[1])
            c = map[r[1]][1]
            must.append(c)

    print(must)