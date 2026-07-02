class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i+1][j] + memo[i][j+1]
        return memo[0][0]