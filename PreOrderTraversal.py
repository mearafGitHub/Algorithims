class Node:
    def __init__(self, val, ):
        self.val = val
        self.left = None
        self.right = None


def preorder(self, root):
    res = []

    def preorderTravelsal(root):
        if not root:
            return
        res.append(root.val)
        preorderTravelsal(root.left)
        preorderTravelsal(root.right)
        return res

    preorderTravelsal(root)
    return res


root = Node(3)
root.left = Node(4)
root.right = Node(5)
p = PreorderT()
print(p.preorder(root))
