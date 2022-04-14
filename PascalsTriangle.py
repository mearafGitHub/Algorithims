class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = [[1]]

        for i in range(1, numRows):
            prevRow = triangle[i - 1]
            newRow = []
            newRow.append(1)

            for j in range(1, i):
                newRow.append(prevRow[j] + prevRow[j - 1])

            newRow.append(1)
            triangle.append(newRow)

        return triangle
