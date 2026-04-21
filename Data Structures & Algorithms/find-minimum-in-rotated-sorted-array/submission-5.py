class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1

        while l < r:
            mid = l + (r-l) // 2

            if nums[mid] > nums[r]:
                # the pivot (min val) must be in top half
                l = mid + 1
            else:
                # not r=mid-1 because it is possible the pivot is at
                # our mid pointer
                r = mid

        return nums[l]