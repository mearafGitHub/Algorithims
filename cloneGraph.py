from collections import defaultdict


class Node:
    def __init__(self, val, neighbours):
        self.val = val
        self.neighbours = neighbours


class Solution:
    clone = Node()

    def BFSClone(node: Node) -> defaultdict(Node):
        parent = {node}
        clone = {node: None}
        new = []
        frontier = [node]
        visited = {node: None}
        i = 1
        level = {}
        while frontier:
            next_front = []
            for u in frontier:
                newclone = Node(u.val)
                for v in node.neighbours:
                    if v not in clone:
                        c = Node(v.val)
                        newclone.neighbours.append(c)
                        next_front.append()
                clone[u] = newclone
                new.append(newclone)
            frontier = next_front
            i += 1
        return (clone, new)

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        result = BFSClone(node)
        return reslult
