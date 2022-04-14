"""
given a string representation of a value remove k numbers to give the smallest possible numbers
"""
def remove(str_num, k):
    # we use a stack to keep the best numbers
    num = []
    for n in str_num:
        while k > 0 and num and num[-1] > n:
            num.pop()
            k -= 1
        num.append(n)
    return num

print(remove('1432219', 3))