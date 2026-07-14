class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        memo1 = 1
        memo2 = 2

        for i in range(n-2):
            memo1, memo2 = memo2, memo1+memo2
        return memo2