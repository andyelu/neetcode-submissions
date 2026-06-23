class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1

        for i in range(n-2, -1, -1):
            curr_longest = 1
            for j in range(i, n):
                if nums[i] < nums[j]:
                    curr_longest = max(curr_longest, 1 + dp[j])
            res = max(res, curr_longest)
            dp[i] = curr_longest
        return res