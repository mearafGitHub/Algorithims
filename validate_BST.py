def validate(root):
    left_bound = float("-inf")
    right_bound = float("inf")

    valid = is_validate(root, left_bound, right_bound)
    return valid


def is_validate(node, lower_bound, upper_bound):
    if not node:
        return True
    if not (node.val < upper_bound and node.val > lower_bound):
        return False

    left_subtree = is_validate(node.left, lower_bound, node.val)
    right_subtree = is_validate(node.right, node.val, upper_bound)
    return left_subtree and right_subtree

