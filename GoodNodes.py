class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def good_nodes(root, maxValue):
    if not root:
        return 0
    goods = 1 if (root.val >= maxValue) else 0
    maxValue = max(root.val, maxValue)
    goods += good_nodes(root.left, maxValue)
    goods += good_nodes(root.right, maxValue)
    return goods


root = Node(0)
root.left = Node(1)
root.right = Node(2)

root.left.left = Node(11)
root.left.right = Node(12)
root.left.right.left = Node(121)
root.left.right.right = Node(3)
root.right.left = Node(21)
root.right.right = Node(22)
print('Uses Depth first search algo')
print('Good nodes:', good_nodes(root, root.val))
print('Time: O(n), space: O(1)')
