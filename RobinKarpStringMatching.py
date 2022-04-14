def hashFunc(pat):
    code = 0
    x = len(pat) - 1
    for p in pat:
        code += ord(p) * (10 ** x)
        x -= 1
    return code


def confirm(pat, sub):
    for i in range(len(pat)):
        if not (pat[i] == sub[i]):
            return False
    return True


def rabin_karp(string, pat):
    if not string or not pat:
        return False
    """
    hash the pattern	
    if the code of the current slice matches, then check the pattern    
    loop through the string applying the hash function on the slice with the size of the pattern
    """
    patCode = hashFunc(pat)
    i = 0
    subCode = hashFunc(string[0:len(pat)])
    while i < len(string) - 1:
        subCode = hashFunc(string[i:i + len(pat)])
        if subCode == patCode:
            sub = string[i:i + len(pat)]
            if confirm(pat, sub):
                return (True, i)
        i += 1

    return (False, i)


# using a hash roll to avoid spurious hits
# O(n-m+1)  -> O(nm) rare worstcase space is constant
print(rabin_karp('chrispat', 'pat'))

