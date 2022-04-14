class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def makeTree(left, right, array):
    if left > right:
        return None

    mid = (left + right) // 2
    root = Node(array[mid])
    root.left = makeTree(left, mid-1, array)
    root.right = makeTree(mid+1, right, array)
    return root

def tree_array(array):

    if not array:
        return None
    tree = makeTree(0, len(array)-1, array)
    return tree

print(tree_array([-10, -3, 0, 5, 9]))