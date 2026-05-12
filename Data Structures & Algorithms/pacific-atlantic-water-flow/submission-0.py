class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []

        max_i = len(heights)
        max_j = len(heights[0])

        p = set()
        a = set()

        def dfs(i,j,visited):
            if (i,j) in visited:
                return

            visited.add((i,j))

            for nei in ((0,1), (0,-1), (1,0), (-1,0)):
                ni, nj = nei[0]+i, nei[1]+j

                if (0 <= ni < max_i
                   and 0 <= nj < max_j
                   and heights[ni][nj] >= heights[i][j]):
                   dfs(ni,nj,visited)

        for i in range(max_i):
            dfs(i,0,p)
            dfs(i,max_j-1,a)
        for j in range(max_j):
            dfs(0,j,p)
            dfs(max_i-1,j,a)

        return [list(c) for c in p & a]
            
