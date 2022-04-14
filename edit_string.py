def edit_y_x(x, y):
    if len(x) <= len(y):
        limit = len(x)
    else:
        limit = len(y)
    yy = []
    xx = []
    for s in x:
        xx.append(s)
    for c in y:
        yy.append(c)

    for i in range(limit):
        if xx[i] != yy[i]:
            yy[i] = xx[i]
    if len(yy) < len(xx):
        for j in range(len(yy), len(xx)):
            yy.append(xx[j])

    return yy


print(edit_y_x('behappy', 'brgots'))

