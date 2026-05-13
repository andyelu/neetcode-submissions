class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if (i,j) in visited:
                return 0

            visited.add((i,j))

            path_sum = 0
            for nei in ((1,0), (-1,0), (0,1), (0,-1)):
                ni = nei[0] + i
                nj = nei[1] + j

                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    path_sum += dfs(ni,nj)
            return 1 + path_sum

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))

        return res
                
