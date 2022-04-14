def gcd(a, b):
    # print(a, b)
    if a == 0:
        return b
    return gcd(b % a, a)


print(gcd(15, 85))
