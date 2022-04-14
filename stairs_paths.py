def stairs(n):
    o, t = 1, 1

    for _ in range(n - 1):
        tep = o
        o = o + t
        t = tep
        print(o, '  ', t)

    return o


print(stairs(5))

#  real dynamc programming
# used memoization and Bottom up to
# simplify it even more
# take advantage of more precise patterns (the core driving patters)