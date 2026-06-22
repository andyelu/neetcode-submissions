class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sub_sums = set([0, nums[0]])
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        for i in range(1, len(nums)):
            to_add = set()
            for num in sub_sums:
                new_sum = num + nums[i]
                if num == target or num + nums[i] == target:
                    return True
                to_add.add(num + nums[i])
            sub_sums.update(to_add)

        return False
            

        

        