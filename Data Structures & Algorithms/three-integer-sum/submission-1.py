class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # this problem becomes a lot simplier when you think of it as
        # an extension of 2sum and 2sum2. In order to avoid duplicates,
        # we can sort the array before we start and then find triplets for
        # only unique a values in [a,b,c]. 

        # why did we sort? Well we need to enforce no duplicate triplets.
        # with a sorted array, we can fix the first number, and then just
        # find the corresponding target two sum with the next two values.

        # sorting lets us easily skip duplicates in the b and c position.
        # we will be applying two pointer, so to do this, we can just use a
        # while loop while inc/dec the indices. Also, because our array is
        # sorted, two pointer allows us to find our target by incrementing
        # either the l or r pointer based on if our target sum is greater
        # or less than what we want

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
                



            

