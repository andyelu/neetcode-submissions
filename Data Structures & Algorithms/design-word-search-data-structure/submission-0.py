class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(start_index, root):
            curr = root

            for i in range(start_index, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c in curr.children:
                        curr = curr.children[c]
                    else:
                        return False
            return curr.is_end

        return dfs(0, self.root)
