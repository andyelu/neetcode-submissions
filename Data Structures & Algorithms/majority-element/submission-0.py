class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums_map = {}

        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1
            if nums_map[num] == n // 2 + 1:
                return num

        

        