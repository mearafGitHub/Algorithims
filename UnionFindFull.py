class Solution:
    def unionFind(self, vertices, edges):  # vertices can be n -> 0 - n
        rank = [1 for _ in vertices]
        root = [i for i in vertices]

        def findRoot(node):
            while node != root[node]:
                root[node] = root[root[node]]
                node = root[node]
            return node

        def findConnection(n1, n2):
            return findRoot(n1) == findRoot(n2)

        def union(A, B):
            rA = findRoot(A)
            rB = findRoot(B)
            if rA != rB:
                if rank[rA] >= rank[rB]:
                    root[rB] == rA
                    rank[rA] += rank[rB]
                else:  # when rA < rB
                    root[rA] == rB
                    rank[rB] += rank[rA]
                return 1
            else:
                return 0

        compNum = len(vertices)
        for u, v in edges:
            compNum -= union(u, v)
        return compNum


v = [0, 1, 2, 3, 4]
e = [[0, 1], [1, 2], [3, 4], [2, 3]]
s = Solution()
print(s.unionFind(v, e))
