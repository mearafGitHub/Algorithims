def is_robot_in_cycle(instruction):
    horzontal, vertical = 0, 1
    x, y = 0, 0

    for i in instruction:
        if i == "G":
            x, y = horzontal + x, vertical + y
        elif i == "L":
            horzontal, vertical = -1 * horzontal, vertical
        elif i == "R":
            horzontal, vertical = horzontal, -1 *vertical
        else:
            print("Wrong Instruction")

    is_cycle = (x, y) == (0, 0) or (vertical, horzontal) != (0, 1)
    return is_cycle

print(is_robot_in_cycle('GRLG'))