class Node:
    def __init__(self, key):
        self.num = key
        self.left = None
        self.right = None


class LCAInt:
    def find_lca(self, root, p, q):
        node = root
        print('current node:  ',node.left.num)
        while node:
            if p.num > node.num and q.num > node.num:
                node = node.right
                print('if: ', node.num)
            elif p.num < node.num and q.num < node.num:
                node = node.left
                print('elif: ', node.num)
            else:
                print('esle: ',node.num)
                return node.num


root = Node(1)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

lca = LCAInt()
print('This solution assumes the node can be its own ancestor.')
print("LCA(4, 5) = ", (lca.find_lca(root, Node(4), Node(5))))

