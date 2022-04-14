def palindrome(s):
    r = s[::-1]
    i = 0
    if s == r:
        return True
    for c in s:
        if i > len(s):
            return -1
        if c != r[i]:
            return s.index(r[i])
        else:
            i += 1


print(palindrome("rori"))