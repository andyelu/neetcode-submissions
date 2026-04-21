class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def findMinHelper(start, end):
            mid = start + (end-start)//2
            mid_val = nums[mid]

            if nums[mid-1] > nums[mid]:
                return nums[mid]

            # recurse to the side with the rotation pivot
            # if this segment is normal, just do regular binary search
            # for the minimum (recurse onto left side)
            if nums[end] < mid_val:
                return findMinHelper(mid+1, end)
            elif nums[start] > mid_val:
                return findMinHelper(start, mid-1)
            else:
                # this must be normal, return first item
                return nums[start]


            return findMinHelper

        return findMinHelper(0, len(nums)-1)
                