class TrieNode:
    def __init__ (self):
        self.children = 26 * [None]
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(root, i):
            if i == len(word):
                return root.endOfWord
            
            c = word[i]

            if c == '.':
                for child in root.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
            else:
                index = ord(c) - ord('a')
                if root.children[index] == None:
                    return False
                return dfs(root.children[index], i + 1)

        return dfs(self.root, 0)






