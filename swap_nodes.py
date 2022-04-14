"""
In-order traversal is performed as

Traverse the left subtree.
Visit root.
Traverse the right subtree.
For this in-order traversal, start from the left child of the root node and keep exploring the left subtree
until you reach a leaf. When you reach a leaf, back up to its parent, check for a right child and visit it if
there is one. If there is not a child, you've explored its left and right subtrees fully. If there is a right child,
traverse its left subtree then its right in the same manner. Keep doing this until you have traversed the entire tree.
You will only store the values of a node as you visit when one of the following is true:

it is the first node visited, the first time visited
it is a leaf, should only be visited once
all of its subtrees have been explored, should only be visited once while this is true
it is the root of the tree, the first time visited
Swapping: Swapping subtrees of a node means that if initially node has left subtree L and right subtree R,
then after swapping, the left subtree will be R and the right subtree, L.

For example, in the following tree, we swap children of node 1.

                                Depth
    1               1            [1]
   / \             / \
  2   3     ->    3   2          [2]
   \   \           \   \
    4   5           5   4        [3]
In-order traversal of left tree is 2 4 1 3 5 and of right tree is 3 5 1 2 4.
"""

from collections import deque

class Node:
    def __init__(self, index):
        self.left = None
        self.right = None
        self.index = index


def in_order_traverse(root):
    """Don't use recursion b/c of recursion limit."""
    stack = deque([root])
    visited = set()
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if node.index in visited:
            print(node.index, end=' ')
            continue
        visited.add(node.index)
        stack.append(node.right)
        stack.append(node)
        stack.append(node.left)


def swap(root, k):
    """Don't use recursion b/c of recursion limit."""
    q = deque([(root, 1)])
    while q:
        node, level = q.popleft()
        if node is None:
            continue
        if level % k == 0:
            node.left, node.right = node.right, node.left
        q.append((node.left, level+1))
        q.append((node.right, level+1))



# get number of nodes
N = int(input())

# create node list
nodes = [None]*(N+1)
for i in range(1, N+1):
    n = Node(i)
    n.left_index, n.right_index = [v if v > 0 else 0 for v in map(int, input().split())]
    nodes[i] = n

# fill out node objects
for n in nodes[1:]:
    left = nodes[n.left_index]
    right = nodes[n.right_index]
    n.left = left
    n.right = right

T = int(input())
root = nodes[1]
# do the swapping
for _ in range(T):
    k = int(input())
    swap(root, k)
    in_order_traverse(root)
    print('')