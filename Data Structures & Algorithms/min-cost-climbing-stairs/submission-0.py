class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = cost[0], cost[1]

        for i in range(2, len(cost)):
            prev, curr = curr, min(prev, curr) + cost[i]

        return min(prev, curr)