class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1

        for i in range(n-2, -1, -1):
            curr_max = 1
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    curr_max = max(curr_max, 1+dp[j])
            dp[i] = curr_max
            res = max(res, curr_max)
        return res