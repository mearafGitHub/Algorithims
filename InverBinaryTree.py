class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=' ')
        if self.right:
            self.right.print_tree()
        print(self.data)


class Solution:
    def invert(self, node):
        if not node:
            return
        node.right = self.invert(node.left)
        node.left = self.invert(node.right)
        return node


Tree = Node(10)
Tree.left = Node(20)
Tree.right = Node(30)
Tree.left.left = Node(40)
Tree.right.right = Node(50)
print('Initial Tree :\n', end= '')
Tree.print_tree()
s = Solution()
s.invert(node=Tree)
print('\nInverted Tree :', end=' ')
Tree.print_tree()
