def first_non_repeating_character(S):
    occurance = {}
    for c in S:
        if c in occurance:
            occurance[c] += 1
        else:
            occurance[c] = 1

    for c in occurance:
        if occurance[c] == 1:
            return c


print(first_non_repeating_character('asdncdddddakaaalajjjdhusasbcdef'))
print(first_non_repeating_character('abcabcdef'))
print(first_non_repeating_character('aabbcc'))
