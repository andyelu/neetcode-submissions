class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        # two pointer approach - we increment or decremement based on the
        # height of our current bars. Since we are reducing area by shrinking
        # distance between the pointers (width), by trying to replace the
        # shortest bar, we can potentially find a greater area

        l,r = 0,len(heights)-1

        while (l < r):
            res = max(res, min(heights[l], heights[r]) * (r-l))

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return res