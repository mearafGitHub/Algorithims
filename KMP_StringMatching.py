# String Matching Krusk’s Moris Pratt Algo:
def kmp_string_matching(needle, heystack):
    if not needle: return 0

    lps = [0 for _ in needle]
    prevLps = 0  # previous prefix setter and pointer to prev char in needle
    i = 1  # current char/symbol pointer

    while i < len(needle):  # building Longest Prefix Suffix array/ ds
        if needle[i] == needle[prevLps]:  # if prefix is found to the left of the current char/symbol
            lps[i] = prevLps + 1
            i += 1
            prevLps += 1
        elif prevLps == 0:  # if no prefix is found at all
            lps[i] = 0
            i += 1
        else:  # if not yet find prifix
            prevLps = lps[prevLps - 1]

    i = 0  # haystack pointer
    j = 0  # needle pointer

    while i < len(heystack):
        if needle[j] == heystack[i]:
            i, j = i + 1, j + 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        if j == len(needle):
            match_index = i - len(needle)
            return match_index
    return -1


needle = 'hey'
heystack = 'heystack'
print(kmp_string_matching(needle, heystack))
