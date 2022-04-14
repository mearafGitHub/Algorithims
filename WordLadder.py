import collections


class Solution:
    def wordLader(self, beginWord: str, endWord: str, wordList: list) -> int:

        def adjancyMap(beginWord: str, endWord: str, wordList: list) -> int:
            queue = collections.deque([beginWord])
            if not endWord == wordList[-1]:
                return -1

            adjacency = {x: [] for x in wordList}
            adjacency[beginWord] = []
            for i in range(len(wordList)):
                if beginWord != wordList[i]:
                    diff = 0
                    j = 0
                    for j in range(len(beginWord)):
                        if beginWord[j] != wordList[i][j]:
                            diff += 1
                            j += 1
                    if diff <= 1:
                        adjacency[beginWord].append(wordList[i])

            k = 1
            m = 0
            while k < len(wordList):
                if wordList[k] != wordList[m]:
                    diff = 0
                    while j < len(wordList[m]):
                        if wordList[m][j] != wordList[k][j]:
                            diff += 1
                    if diff <= 1:
                        adjacency[wordList[m]].append(wordList[k])
                k, m = k + 1, m + 1

            return adjacency

        adj = adjancyMap(beginWord, endWord, wordList)
        word = [beginWord, adj[beginWord]]
        transformation = []  # O(n) space
        while word:  # O(n+m) time m-> some diplicates
            transformation.append(word[0])
            if not word[1]:
                word = []
            else:
                word = [word[1][0], adj[word[1][0]]]
        return (transformation, len(transformation))
