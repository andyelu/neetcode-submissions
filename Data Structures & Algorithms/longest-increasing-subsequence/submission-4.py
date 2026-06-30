class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {n:0}
        res = 0

        def dfs(i):
            nonlocal res
            if i in dp:
                return dp[i]

            curr_max = 1
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    curr_max = max(curr_max, 1+dfs(j))
            res = max(res, curr_max)

            dp[i] = curr_max
            return curr_max

        for i in range(n):
            dfs(i)
        return res