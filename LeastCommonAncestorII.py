class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class FindLCA:
    def lca(self, root, val1, val2):

        def find(root, val):
            if not root:
                return False
            if root.val == val:
                return True
            # print(find(root.left, val) or find(root.right, val))
            if find(root.left, val) or find(root.right, val):
                return True
            return False
