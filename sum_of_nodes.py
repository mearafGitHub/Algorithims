def sum_of_nodes(root):
    sum = 0
    if root is None:
        return 0
    nodes = [root]
    while nodes:
        node = nodes.pop()
        sum += node.data
        if node.right:
            nodes.append(node.right)
        if node.left:
            nodes.append(node.left)
    return sum