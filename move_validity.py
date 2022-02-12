grid = [
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1]
]


# store position information when found
# of each robots in list in tuples
def store_position_inf(grid):
    valid_move = 1
    all_positions = []
    # positions = []
    for row in grid:
        step_positions = []
        en_r = enumerate(row)
        for count, item in en_r:
            if item == valid_move:
                step_positions.append(count)

        all_positions.append(step_positions)
        print("\n\n")
    print(all_positions)
    validate_moves(all_positions)


def validate_moves(all_positions):
    # go through all_postions and then each positions
    # compair the current to the next
    for i in range(0, len(all_positions) - 1):
        moves = [item[i] for item in all_positions]
        if abs((moves[i] - moves[i + 1])) == 0 or (abs(moves[i] - moves[i + 1])) == 1:
            print("Valid")

        elif abs((moves[i] - moves[i + 1])) > 1:
            print("Invalid")


# return "invalied move from: ",pos[p]," ==> ",pos[p-1]

store_position_inf(grid)