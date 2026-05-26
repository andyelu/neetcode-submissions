class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dp(first, end):
            a, b = 0, 0

            for i in range(first, end):
                a, b = b, max(a + nums[i], b)

            return b

        return max(dp(0, len(nums)-1), dp(1, len(nums)))