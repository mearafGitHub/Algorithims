class Trie:
    def __int__(self):
        self.children = {}
        self.isWord = False


class WordAddSearch:
    def __init__(self):
        self.root = Trie()

    def add(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        def subsearch(j, node):
            cur = node
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for child in cur.children.values():
                        if subsearch(i+1, child):
                            return True
                    return False
                else:
                    if char not in cur.children.values():
                        return False
                    cur = cur.children[char]

            return cur.isWord

        return subsearch(0, self.root)


ws = WordAddSearch()
board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain", ["o", "e", "i", "i", "i", "i"]]
for word in words:
    ws.add(words)
print(ws.search(board, words))
