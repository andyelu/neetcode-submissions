class Solution:
    def findMin(self, nums: List[int]) -> int:
        # with this problem, you are essentially searching for the pivot
        # with binary search. You find the pivot by doing comparisons between
        # the mid value and the l and r values. The rotation breaks sorted order (unless
        # sorted n times), so we shrink our window to the right if nums[r] < mid --
        # left otherwise. A distinction in the way we are doing binary search
        # here is that we don't exclude mid each time we make a smaller window.
        # It is important to note that if our mid value happens to be the pivot,
        # we will focus on the right side -- we don't exclude mid index here because
        # it can be our pivot

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