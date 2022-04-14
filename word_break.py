#  see if the broken words in  a given string s, are found in  the given word_dict
#  DP with Bottum-up


def word_break(word_dict, s):
    memo = [False] * (len(s)+1)
    memo[len(s)] = True
    print(memo)

    for i in range(len(s)-1, -1, -1):
        for w in word_dict:
            if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                memo[i] = memo[i + len(w)]
            if memo[i]:
                break
        return memo[0]


def wordBreak(wordList, word):
    if word == '':
        return True
    else:
        wordLen = len(word)
        return any([(word[:i] in wordList) and wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)])

print(wordBreak(['code', 'dp', 'time', 'linear'], 'codetime'))