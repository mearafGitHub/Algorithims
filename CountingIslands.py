class Solution:
    def numIslands(self, grid) -> int:

        def negihbours(grid, i, j):

            if i < 0 or i >= (len(grid)) or j < 0 or j >= (len(grid[i])) or grid[i][j] == "0":
                return

            grid[i][j] = '0'

            negihbours(grid, i - 1, j)  # up
            negihbours(grid, i + 1, j)  # down
            negihbours(grid, i, j - 1)  # left
            negihbours(grid, i, j + 1)  # right

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islands += 1
                    negihbours(grid, i, j)

        return islands

