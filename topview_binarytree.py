from collections import defaultdict

def topView(root):
    # Write your code here
    if root is None:
        return None
    queue = [(root, 0)]
    hashtable = defaultdict(list)
    for node, level in queue:
        if node is not None:
            hashtable[level].append(node.info)
        if node.left is not None:
            queue.extend([(node.left, level - 1)])
        if node.right is not None:
            queue.extend([(node.right, level + 1)])
    if hashtable:
        for level in range(min(hashtable.keys()), max(hashtable.keys()) + 1):
            print(hashtable[level][0], end=' ')
    else:
        return None