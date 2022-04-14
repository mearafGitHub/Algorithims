class Solution:
    def solve(self, A):

        A.sort()
        remove = 0
        prevEnd = A[0][1]

        for start, end in A:
            if start > prevEnd:
                prevEnd = end
            else:
                prevEnd = min(end, prevEnd)
                remove += 1
        return (len(A) - remove) + 1
