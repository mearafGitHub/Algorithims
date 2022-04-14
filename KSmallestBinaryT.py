class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class SmallestInBinaryTreeL:

    def inorder(self, root, k):
        stack = []
        n = 0
        cur = root
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            n += 1
            print('n: ', n, '  cur: ', cur.val)
            if n == k:
                return res

            cur = cur.right

        return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

s = SmallestInBinaryTreeL()

print(s.inorder(root, 4))