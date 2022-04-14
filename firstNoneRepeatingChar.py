def first_non_repeating_character(S):
    occurrence = {}
    for c in S:
        if c in occurrence:
            occurrence[c] += 1
        else:
            occurrence[c] = 1

    for c in occurrence:
        if occurrence[c] == 1:
            return c


print(first_non_repeating_character('asdncdddddakaaalajjjdhusasbcdef'))
print(first_non_repeating_character('abcabcdef'))
print(first_non_repeating_character('aabbcc'))
