class TrieNode():
    def __init__(self):
        self.endOfWord = False
        self.children = [None] * 26

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root

        for c in word:
            index = ord(c) - ord('a')
            if root.children[index] == None:
                root.children[index] = TrieNode()
            root = root.children[index]
        root.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            curr = node

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children:
                        if child and dfs(i + 1, child):
                            return True
                    return False
                else:
                    index = ord(c) - ord('a')
                    if curr.children[index] is None:
                        return False
                    curr = curr.children[index]

            return curr.endOfWord

        return dfs(0, self.root)