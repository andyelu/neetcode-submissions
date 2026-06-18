class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}

        def helper(val):
            if val == 0:
                return 0

            res = float("inf")
            for coin in coins:
                if val-coin < 0:
                    continue                    

                if val-coin not in memo:
                    helper(val-coin)
                if memo[val-coin] == -1:
                    continue

                res = min(res, 1 + memo[val-coin])

            memo[val] = res if res < float("inf") else -1
            return memo[val]

        return helper(amount)
        
