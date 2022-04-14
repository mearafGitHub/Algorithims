import pprint

visited = set()


def bfs(s, grid):
    parent = {s: None}
    level = {s: 1}
    frontier = [s]
    land = []
    visited.add(s)
    x = 1
    cols = len(grid[0])
    rows = len(grid)
    while frontier:
        next_front = []
        adjacent = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for u in frontier:
            r, c = u
            for adjR, adjC in adjacent:
                r, c = r + adjR, c + adjC
                if (r in range(rows) and
                        c in range(cols) and
                        (r, c) not in visited and
                        grid[r][c] == 1):
                    # print("grid[r][c] :  ",grid[r][c], ' | ', (r,c))
                    parent[(r, c)] = u
                    level[(r, c)] = x
                    land.append((r, c))
                    visited.add((r, c))
                    next_front.append((r, c))

        frontier = next_front
        x += 1

    print('Parent: ', parent)
    return parent


def islands(grid):
    # adj = {(i,j): [] for i in range(len(grid)) for j in range(len(grid[i]))}
    islands_index = []
    islands = 0
    if not grid:
        return 0
    i, j = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1 and (i, j) not in visited:
                # expand on the land in bfs while its a land
                land = bfs((i, j), grid)
                islands += 1
                islands_index.append(land)
    return (islands, islands_index)


grid_ = [
    [1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 1]]
pp = pprint.PrettyPrinter(indent=3)
print()
pp.pprint(islands(grid_))