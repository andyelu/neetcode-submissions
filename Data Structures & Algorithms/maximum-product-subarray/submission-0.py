class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        memo = [[1,1] for _ in range(n)]

        if n == 1:
            return res

        memo[0][0], memo[0][1] = nums[0], nums[0]

        for i in range(1,n):
            memo[i][0] = max(nums[i], memo[i-1][0] * nums[i], memo[i-1][1] * nums[i])
            memo[i][1] = min(nums[i], memo[i-1][0] * nums[i], memo[i-1][1] * nums[i])
            res = max(memo[i][0], res)

        return res
