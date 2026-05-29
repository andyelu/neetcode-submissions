class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.last_added_child = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                curr.last_added_child = c
            curr = curr.children[c]

        curr.is_end = True
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        trie = Trie()
        for s in strs:
            trie.add(s)

        curr = trie.root
        while curr and not curr.is_end and len(curr.children) == 1:
            res += curr.last_added_child
            curr = curr.children[curr.last_added_child]

        return res

