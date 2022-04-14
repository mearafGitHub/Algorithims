class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


path = {}
a = []
parent = None


def findRoots(root, n, depth=0):
    if root is None:
        return

    global parent
    global path
    # print('Node: ', root.key, '  depth:  ', depth, '  parent: ', parent)

    if root.key not in path:
        path[root.key] = [parent, depth]
    if root.key == n:
        return path

    depth += 1
    parent = root.key
    findRoots(root.left if root.left else None, n, depth)
    parent = root.key
    findRoots(root.right if root.right else None, n, depth)

    return path


def findLCA(root, a, b):
    findRoots(root, a)
    findRoots(root, b)
    return lca(a, b)


def lca(a, b):
    if path[a][0] is None and path[b][0] is None:
        return None
    elif path[a][0]:
        return path[a][0]
    elif path[b][0]:
        return path[b][0]
    elif path[a][0] == path[b][0]:
        print("Found LCA: ", path[b][0])
        return path[b][0]
    else:
        lca(path[a][0], path[b][0])



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


print("LCA(4, 5) = ", (findLCA(root, 4, 5,)))
print("LCA(4, 6) = ", (findLCA(root, 4, 6)))
print("LCA(3, 4) = ", (findLCA(root, 3, 4)))
print("LCA(4, 7) = ", (findLCA(root, 4, 7)))
