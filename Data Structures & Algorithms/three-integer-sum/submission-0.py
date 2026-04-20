class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        i = 0
        while i < len(nums):
            target = -nums[i]

            if target < 0:
                return res

            l = i+1
            r = len(nums) - 1

            while l < r:
                cur_sum = nums[l] + nums[r]
                if cur_sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                if cur_sum > target:
                    cur_r_val = nums[r]
                    while l < r and nums[r] == cur_r_val:
                        r -= 1
                else:
                    cur_l_val = nums[l]
                    while l < r and nums[l] == cur_l_val:
                        l += 1
            
            cur_i_val = nums[i]
            while i < len(nums) and nums[i] == cur_i_val:
                i += 1
        
        return res
                



            

