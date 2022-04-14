def max_unit(box_types, t):
    load = 0
    # sort and start from the last if the bigger boxes has priority
    for box in box_types:
        b, u = box
        if t > 0:
            if t >= b:
                load += b * u
                t -= 1
            else:
                dif = b - t
                load += dif * u
                # t -= 1
                break

    return (load)

print(max_unit([[1,3], [2,2],[3,1]], 4))
