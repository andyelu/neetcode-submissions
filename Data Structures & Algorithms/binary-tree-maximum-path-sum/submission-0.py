# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float('-inf')]

        def maxPathSumHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = maxPathSumHelper(root.left)
            right = maxPathSumHelper(root.right)
            max_root_path_nb = max(root.val+left, root.val+right, root.val)

            max_sum[0] = max(max_root_path_nb, root.val+left+right, max_sum[0])

            return max_root_path_nb

        maxPathSumHelper(root)

        return max_sum[0]