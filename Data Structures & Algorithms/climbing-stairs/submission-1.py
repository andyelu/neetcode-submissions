class Solution:
    memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if n-1 not in self.memo:
            self.memo[n-1] = self.climbStairs(n-1)

        if n-2 not in self.memo:
            self.memo[n-2] = self.climbStairs(n-1)

        return self.memo[n-1] + self.memo[n-2]