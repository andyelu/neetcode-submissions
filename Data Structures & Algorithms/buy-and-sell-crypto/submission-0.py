class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer, l will represent buy day, r will represent sell day
        # update l to be r when profit is negative
        max_profit = 0

        l,r = 0,0

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit <= 0:
                l = r
            else:
                max_profit = max(max_profit, profit)

            r += 1

        return max_profit