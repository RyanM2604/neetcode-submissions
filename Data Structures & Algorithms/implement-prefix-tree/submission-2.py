class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root

        for c in word:
            index = ord(c) - ord('a')
            if root.children[index] == None:
                root.children[index] = TrieNode()
            root = root.children[index]
        root.endOfWord = True

    def search(self, word: str) -> bool:
        root = self.root

        for c in word:
            index = ord(c) - ord('a')
            if root.children[index] == None:
                return False
            root = root.children[index]
        return root.endOfWord

    def startsWith(self, prefix: str) -> bool:
        root = self.root

        for c in prefix:
            index = ord(c) - ord('a')
            if root.children[index] == None:
                return False
            root = root.children[index]
        return True
        