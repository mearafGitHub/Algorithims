"""
Build a tree from preorder and inorder traversal, fiven arrayys for both.
"""

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class BuildTree:
    def build(self, preorder, inorder):
        if not preorder and not inorder:
            return None

        io = {}
        j = 0
        for i in inorder:
            io[i] = j
            j += 1

        root = Node(preorder[0])
        mid = io[preorder[0]]

        root.left = self.build(preorder[1:mid + 1], inorder[:mid])
        root.right = self.build(preorder[mid + 1:], inorder[mid + 1:])

        return root


tr = []

def build(preorder, inorder):
    if not preorder and not inorder:
        return None
    #  used a dictionary to save index searching time in inorder traversal
    io = {}
    j = 0
    for i in inorder:
        io[i] = j
        j += 1

    root = Node(preorder[0])
    mid = io[preorder[0]]
    tr.append(root.val)
    root.left = build(preorder[1:mid + 1], inorder[:mid])
    root.right = build(preorder[mid + 1:], inorder[mid + 1:])

    return root


tree = build([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
# print((tree.left.val, tree.right.val))
print(tr)
