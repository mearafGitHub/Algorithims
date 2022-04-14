def bestSell(stoke):
    l, r = 0, 1

    best = stoke[r] - stoke[l]

    while r < len(stoke):
        profit = stoke[r] - stoke[l]
        if profit >= 0:
            best = max(best, profit)
        else:
            l = r
        r += 1

    return best


print(bestSell([7, 4, 3, 8, 12, 9]))
