class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited_path = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, word_ptr):
            if word_ptr == len(word):
                return True

            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                word[word_ptr] != board[r][c] or
                (r,c) in visited_path):
                    return False

            visited_path.add((r,c))
            word_ptr += 1

            if (dfs(r-1, c, word_ptr) or
                dfs(r+1, c, word_ptr) or
                dfs(r, c-1, word_ptr) or
                dfs(r, c+1, word_ptr)):
                    return True
            else:
                visited_path.remove((r,c))
                word_ptr -= 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if (dfs(r, c, 0)):
                    return True

        return False
                    
            