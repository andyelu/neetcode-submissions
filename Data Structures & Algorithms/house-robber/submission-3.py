class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        for i in range(len(nums)):
            a = 0 if i < 2 else dp[i-2]
            b = 0 if i < 1 else dp[i-1]

            dp[i] = max(a + nums[i], b)

        return dp[-1]