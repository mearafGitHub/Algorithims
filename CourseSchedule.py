# preq = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
preq = [[0, 1], [1, 0]]
visited = []
parent = {}


def canFinish(edges, num):  # num = number of course
    pre = {i: [] for i in range(num)}
    for c, p in edges:
        pre[c].append(p)
    print(pre)
    r = dfs(pre)
    return r


def dfs(pre):
    for crs, adj_pre in pre.items():
        print('parent:  ', parent)
        print('visited:  ', visited)
        if crs not in visited:
            visited.append(crs)
            if crs not in parent:
                parent[crs] = None
            if not adj_pre == []:
                for item in adj_pre:
                    print('preq:  ', item)
                    res = dfs_depth(pre, item)
                    print('res:  ', res)
                    if res == False:
                        return False
                    if res == True:
                        pre[crs].remove(item)
    return tuple(True, visited[::-1])


def dfs_depth(pre, i):
    global parent
    if not pre[i]:
        visited.append(i)
        return True
    else:
        for v in pre[i]:
            if v not in parent:
                print('v:  ', v)
            elif v in visited:
                if v in parent:
                    return False
            if v not in visited:
                visited.append(i)
                dfs_depth(pre, v)
    return True


print(canFinish(preq, 5))
