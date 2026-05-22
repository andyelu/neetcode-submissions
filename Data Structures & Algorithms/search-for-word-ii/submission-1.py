class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add_word(w)

        res = set()

        m = len(board)
        n = len(board[0])

        def dfs(root, i, j, visited_path, curr_word):
            c = board[i][j]
            if c not in root.children:
                return
            
            nxt = root.children[c]
            curr_word += c
            visited_path.add((i,j))
            
            if nxt.is_end:
                res.add(curr_word)

            for nei in ((0,1), (1,0), (-1,0), (0,-1)):
                ni = nei[0] + i
                nj = nei[1] + j

                if ((ni,nj) not in visited_path and 
                    0 <= ni < m and 
                    0 <= nj < n): 
                    dfs(root.children[c], ni, nj, visited_path, curr_word)
            visited_path.remove((i,j))

        for i in range(m):
            for j in range(n):
                dfs(trie.root, i, j, set(), "")

        return list(res)
            