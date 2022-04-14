class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

"""
 "." dot character matches any character
"""


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                # store each letter/symbol/char in the children dict of the current node
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.end = True

    def search(self, word):
        # recursion needed for the operation in the case of '.'
        def dfs_(i, root):
            cur = root
            for j in range(i, len(word)):
                w = word[j]
                if w == '.':
                    for child in cur.children.values():
                        if dfs_(j+1, child):
                            return True
                    return False
                else:
                    if w not in cur.children:
                        return False
                cur = cur.children[w]
            return cur.end
        return dfs_(0, self.root)

    def start_with(self, prefix):
        cur = self.root
        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return True

