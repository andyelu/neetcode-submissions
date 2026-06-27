class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        dp = [1] * n

        for i in range(n-1, -1, -1):
            curr_lis = 1
            for j in range(i, n):
                if nums[j] > nums[i]:
                    curr_lis = max(curr_lis, 1 + dp[j])
            dp[i] = curr_lis
            res = max(res, curr_lis)
        return res
