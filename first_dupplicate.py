def first_dupplicate(S):
    occurance = {}
    for c in S:
        if c in occurance:
            occurance[c] += 1
        else:
            occurance[c] = 1

    for c in occurance:
        if occurance[c] > 1:
            return (c, occurance[c] )


print(first_dupplicate('asdncdddddakaaalajjjdhusasbcdef'))
print(first_dupplicate('cccabcabcdef'))
print(first_dupplicate('zzzaabbcc'))