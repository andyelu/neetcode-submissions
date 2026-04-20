class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(i, currentList, total):
            if (total == target):
                res.append(currentList.copy())
                return

            for j in range(i, len(nums)):
                if (total + nums[j] > target):
                    break
                currentList.append(nums[j])
                dfs(j, currentList, total + nums[j])
                currentList.pop()

        dfs(0, [], 0)
        return res