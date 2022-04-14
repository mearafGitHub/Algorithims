def onesI(n):
    count = 0
    while n > 0:
        count += n % 2
        n = n >> 1
    return count


def onesII(n):  # runs only when it finds one; number of '1's in n before n becomes 0
    count = 0
    while n > 0:
        count += 1
        n &= (n-1)
    return count
