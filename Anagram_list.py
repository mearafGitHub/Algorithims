from collections import defaultdict


def anagrams(words):
    # key value pair, key: a list of letter occurrence and value is the list of words with that occurrence
    groups = defaultdict(list)
    for word in words:
        count = [0] * 26
        for c in word:  # counting occurrence of each letter and storing that pattern of each word in a list
            count[ord(c) - ord('a')] += 1
        groups[tuple(count)].append(word)   # update dictionary each letter pattern -> key, occurrence -> value
    return groups.values()


print(anagrams(['eat', 'tea', 'car', 'rac', 'tire', 'rite']))

