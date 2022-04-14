"""
give a root of a tree find the max depth
"""
# dfs algo
from collections import deque


def max_depth(root):
    d: int = 0
    if root is None:
        return d
    # take the max of the depth of the left and the right subtrees
    d = 1 + max(max_depth(root.left), max_depth(root.right))
    return d


# bfs algo als for level by level traversal
def max_depthBFS(root):
    # depth and level are same/equal when level by level traversal
    level = 0
    if root is None:
        return level
    q = deque([root])

    while q:
        level += 1
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return level


def max_depthDFSIter(root):
    depth = 0
    trace = [[root, depth]]

    while trace:
        node, d = trace.pop()
        if node:
            depth = max(depth, d)
            trace.append(node.left, d+1)
            trace.append(node.right, d+1)
    return depth


