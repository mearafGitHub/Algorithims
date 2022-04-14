import  os

"""
For each test case, on a separate 
line print YES if it is possible to rearrange 
the grid alphabetically ascending in both its rows and columns, or NO otherwise.
"""

def gridChallenge(n, grid):
    # Write your code here
    prev = ''
    col_prev = ''
    row_dis = False
    clm_dis = False
    idx = -1
    for item in grid:
        for i in item:
            col_prev = i
            prev = i
            if col_prev > i:
                clm_dis = True
            elif col_prev < i:
                clm_dis = False
            if i > prev and (not row_dis):
                prev = i
                continue
            elif i > prev and row_dis:
                row_dis = False
                continue
            elif i < prev:
                idx = item.index(i)
                row_dis = True
                continue

    if not (row_dis and clm_dis):
        return 'YES'
    else:
        return 'NO'
        # return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(n, grid)

        fptr.write(result + '\n')

    fptr.close()
