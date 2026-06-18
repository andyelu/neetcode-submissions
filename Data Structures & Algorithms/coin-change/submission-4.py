class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}

        def helper(val):
            if val in memo:
                return memo[val]

            res = float("inf")
            for coin in coins:
                if val-coin < 0:
                    continue                    

                sub = helper(val-coin)
                if sub == -1:
                    continue

                res = min(res, 1 + memo[val-coin])

            memo[val] = res if res < float("inf") else -1
            return memo[val]

        return helper(amount)
        
