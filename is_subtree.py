"""
tell is a tree is a subtree of a tree, given both trees
"""


def is_same(tree, sub):
    if not tree and not sub:
        return True
    if tree and sub and tree.val == sub.val:
        is_left = is_subtree(tree.left, sub.left)
        is_right = is_subtree(tree.right, sub.right)

        return (is_left and is_right)


def is_subtree(tree, sub):
    if not sub:
        return True
    if not tree:
        return False

    if is_same(tree, sub):
        return True

    else:
        left = is_subtree(tree.left, sub)
        right = is_subtree(tree.right, sub)
        return (left or right)



