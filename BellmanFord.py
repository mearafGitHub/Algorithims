class Vertex:
    def __init__(self):
        self.p = None
        self.distance = float('inf')


w = {}


def weight(i, j):
    if (i, j) in w:
        return w[(i, j)]


def relax(u, v):
    if u.distance > v.distance + weight(v, u):
        u.distance = v.distance + weight(v, u)
        u.p = v


def BellmanFord(V, E, source):
    source.distance = 0
    for i in range(1, len(V)-1):
        for (u, v) in E:
            relax(u, v)


print('Best for negative weight edges. \nO(∣V∣⋅∣E∣) => worst case, O(∣E∣) => Best case.')
