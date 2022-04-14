class Node:
    def __init__(self, val, ):
        self.val = val
        self.left = None
        self.right = None

def inorder(self, root):
    res = []
    def inorderTravelsal(root):
        if not root:
            return
        inorderTravelsal(root.left)
        res.append(root.val)
        inorderTravelsal(root.right)
        return res

    inorderTravelsal(root)
    return res


root = Node(3)

root.left = Node(4)
root.right = Node(5)

print(inorder(root))
