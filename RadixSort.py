def flatten(B):
    A = []
    for b in B:
        if not b:
            continue
        for i in b:
            A.append(i)
    return A

def get_digits(item):
    return len(str(item))

def radix(A):
    digits = get_digits(max(A))
    C = []
    for d in range(digits):
        B = [[] for _ in range(10)]
        e = 10 ** d
        for a in A:
            index = a // e % 10
            B[index].append(a)
            print(index, a, B)
        C = flatten(B)
    return C


# print(flatten([[], [], [12, 14, 25], [31, 11]]))
print(radix([900, 1000, 10, 2000, 4002]))
