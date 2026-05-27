# this problem is literally an extension of house robber 1 solution
# we compare dp(0, len(nums)-1) and dp(1, len(nums)), as these array
# slices force the dp to respect the circular neighbor relationship

# runtime is O(n), as we traverse n-1 elements twice. space is O(1),
# we don't need a memo array if we only require the last 2 values
# for lookback

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dp(start, end):
            a, b = 0, 0
            
            for i in range(start, end):
                a, b = b, max(a + nums[i], b)

            return b

        return max(dp(0, len(nums)-1), dp(1, len(nums)))
                
