import collections

class Node:
    def __init__(self, val, ):
        self.val = val
        self.left = None
        self.right = None


def levelorder(self, root):  # breadth first search algo
    res = []
    q = collections.deque()
    q.append(root)
    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res


root = Node(3)

root.left = Node(4)
root.right = Node(5)
# Time O(n) the same for space complexity
print(levelorder(root))
