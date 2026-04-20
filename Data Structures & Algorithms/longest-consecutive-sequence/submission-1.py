class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if num - 1 doens't exist in nums, that means
        # num is a start of a consecutive sequence
        nums_set = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in nums_set:
                length = 0
                while (n+length) in nums_set:
                    length += 1
                longest = max(length, longest)
        
        return longest
                