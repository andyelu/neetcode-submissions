class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def findMinHelper(start, end):
            mid = start + (end-start)//2
            mid_val = nums[mid]

            if start >= end:
                return nums[start]

            if nums[end] < mid_val:
                return findMinHelper(mid+1, end)
            return findMinHelper(start, mid)

        return findMinHelper(0, len(nums)-1)
                