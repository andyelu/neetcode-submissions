class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n
        res = 1

        for i in range(n-2, -1, -1):
            curr_lis = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    curr_lis = max(curr_lis, 1 + memo[j])
            res = max(res, curr_lis)
            memo[i] = curr_lis
        
        return res
        
            