from collections import defaultdict


def is_valid_sudoku(sudoku):
    row = defaultdict(set)
    col = defaultdict(set)
    sub = defaultdict(set)

    for r in range(9):
        for c in range(9):
            x = sudoku[r][c]
            sr, sc = r // 3, c // 3
            if x == ' ':
                continue
            if x in row[r] or x in col[c] or x in sub[sr][sc]:
                return False
            col[c].add(x)
            row[r].add(x)
            sub[sr][sc].add(x)

    return True
