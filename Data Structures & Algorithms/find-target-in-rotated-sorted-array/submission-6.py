class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while (l <= r):
            mid = l + (r-l) // 2
            mid_val = nums[mid]

            if (mid_val == target):
                return mid

            # check if the left window is sorted
            if (nums[l] <= mid_val):
                # check if target falls in here,
                # otherwise must be in the right window
                if (nums[l] <= target and target <= mid_val):
                    r = mid-1
                else:
                    l = mid+1
            else:
                # check if target falls in the sorted right window
                # otherwise must be in the left window
                if (nums[r] >= target and target >= mid_val):
                    l = mid+1
                else:
                    r = mid-1

        return -1
            
