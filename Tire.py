class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

# Trier is called a prefix tree


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                # store each letter/symbol/char in the children dict of the current node
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.end = True

    def search(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.end

    def start_with(self, prefix):
        cur = self.root
        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        # return cur
        return True


root = TrieNode()


def insert(word):
    cur = root
    for w in word:
        if w not in cur.children:
            # store each letter/symbol/char in the children dict of the current node
            cur.children[w] = TrieNode()
        cur = cur.children[w]
    cur.end = True
    return root


def search(word):
    cur = root
    for w in word:
        if w not in cur.children:
            return False
        cur = cur.children[w]
    return cur.end


def start_with(prefix):
    cur = root
    main = None
    for w in prefix:
        if w == prefix[0] and w in cur.children:
            main = cur.children[w]
        if w not in cur.children:
            return False
        cur = cur.children[w]
    # return main
    return True


def get(cur):
    word = ''
    while cur:
        for child, node in cur.children.items():
            cur = node
            word += child
    return word


data = ['mouse', 'mouse_pad', 'amazon', 'google', 'group', 'zam']
for w in data:
   insert(w)

prefix = 'g'
words = []
word = prefix
cur = start_with(prefix)
if not cur:
    print("Not found")

if cur != False:
    print(cur.children.items())
    while cur.children:
        word += get(cur)
        words.append(word)

print(words)
