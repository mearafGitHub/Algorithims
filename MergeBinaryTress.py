class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def print_tree(self):
        if self.left:
            # print(self.val, end=' -> ')
            self.left.print_tree()
        print(self.val, end=' | ')
        if self.right:
            # print(self.val, end=' | ')
            self.right.print_tree()
        print(self.val, end=' , ')


def MergeBT(root1, root2):
    if not root1 and not root2:
        return None

    rval1 = root1.val if root1 else 0
    rval2 = root2.val if root2 else 0

    new_root = Node(rval1 + rval2)
    new_root.left = MergeBT(root1.left if root1 else None, root2.left if root2 else None)
    new_root.right = MergeBT(root1.right if root1 else None, root2.right if root2 else None)

    return new_root


rootx = Node(0)
rootx.left = Node(1)
rootx.right = Node(2)

rootx.left.left = Node(11)
rootx.left.right = Node(12)
rootx.right.left = Node(21)
rootx.right.right = Node(22)

rootx.left.right.left = Node(121)
rootx.left.right.right = Node(3)


rooty = Node(0)
rooty.left = Node(1)
rooty.right = Node(2)

rooty.left.left = Node(11)
rooty.left.right = Node(12)
rooty.right.left = Node(21)
rooty.right.right = Node(22)

rooty.left.right.left = Node(121)
rooty.left.left.left = Node(120)

rooty.left.right.right = Node(3)


tree = MergeBT(rootx, rooty)
tree.print_tree()
