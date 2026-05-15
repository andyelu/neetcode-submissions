class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs from each treasure chest -> traverse on areas greater than distance from treasure
        # when you traverse to these, update the area value to be the distance treasure

        # here, I use the queue elements to store the distance from the node to treasure
        # remember that unlike dfs, can't have a variable outside the loop to hold distance.
        # essentially, it would lead to this variable being increased every pop, which doesn't
        # match behavior of bfs.
        # each element in queue needs to remember its distance

        m,n = len(grid), len(grid[0])

        def bfs(i,j):
            queue = deque()
            visited = set()

            queue.append((i,j,0))

            while queue:
                curr = queue.popleft()

                grid[curr[0]][curr[1]] = curr[2]
                visited.add(curr)

                for nei in ((1,0), (-1,0), (0,1), (0,-1)):
                    ni = nei[0] + curr[0]
                    nj = nei[1] + curr[1]

                    if (ni,nj) not in visited and 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > curr[2]+1:
                        queue.append((ni,nj,curr[2]+1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(i,j)




