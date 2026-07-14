class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo1 = cost[0]
        memo2 = cost[1]

        for i in range(2, len(cost)):
            memo1, memo2 = memo2, min(memo1,memo2)+cost[i]

        return min(memo1,memo2)