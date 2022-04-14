class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word):
        trie = self
        for w in word:
            if w not in trie.children:
                trie.children[w] = Trie()
            trie = trie.children[w]
        trie.isEnd = True


class WordSearch:
    def wordSearch(self, board, words):
        root = Trie()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])

        res = set()
        visited = set()

        def dfs(r, c, word_, node):
            if (r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited or board[r][c] not in node.children):
                return False
            visited.add((r, c))
            node = node.children[board[r][c]]
            word_ += board[r][c]

            if node.isEnd:
                res.add(word_)

            dfs(r, c-1, word_, node)
            dfs(r, c+1, word_, node)
            dfs(r-1, c, word_, node)
            dfs(r+1, c, word_, node)

            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, '', root)

        return list(res)


ws = WordSearch()
board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain", ["o", "e", "i", "i", "i", "i"]]

print(ws.wordSearch(board, words))
