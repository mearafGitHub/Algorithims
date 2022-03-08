class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def BalacedBinaryTree(root):
    if not root:
        return [True, 0]

    left = BalacedBinaryTree(root.left)
    right = BalacedBinaryTree(root.right)

    is_balanced = (abs(left[1] - right[1]) <= 1 and (left[0] and right[0]))
    height = 1 + max(left[1], right[1])
    return [is_balanced, height]


root = Node(0)
root.left = Node(1)
root.right = Node(2)

root.left.left = Node(11)
root.left.right = Node(12)
root.left.right.left = Node(121)
root.left.right.right = Node(122)
# root.right.left = Node(21)
# root.right.left = Node(22)
print(BalacedBinaryTree(root))
print('Time: O(n) , space: O(1)')
