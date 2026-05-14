class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # run dfs on O's on the border
        # set these to temps -> DFS to search for more O's, setting these to temps as well
        # then loop through board elements, change all O's to X's -- the O's left
        # were the ones that were surrounded

        m,n = len(board), len(board[0])
        visited = set()

        def dfs(i,j):
            if (i,j) in visited or board[i][j] != 'O':
                return
            
            board[i][j] = 'T'
            visited.add((i,j))

            for nei in ((1,0), (0,1), (-1,0), (0,-1)):
                ni = nei[0] + i
                nj = nei[1] + j

                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                    dfs(ni,nj)

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)

        for r in range(2):
            for i in range(m):
                for j in range(n):
                    if r == 0:
                        # first change all O's to X's
                        if board[i][j] == 'O':
                            board[i][j] = 'X'
                    else:
                        # then change all T's back to O's
                        if board[i][j] == 'T':
                            board[i][j] = 'O'

                
