# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float('-inf')]  # single element list so we can reference from inner helper

        # this function returns the max path starting from the root node
        def maxPathSumHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            # find max sum starting from root.left
            left = maxPathSumHelper(root.left)

            # find max sum starting from root.right
            right = maxPathSumHelper(root.right)

            # find the max sum from root without branching -- this needs to be returned
            # we cannot return val + left + right because paths cannot branch
            max_root_path_nb = max(root.val+left, root.val+right, root.val)

            # update our max sum with 3 canditates: the max sum from root without branching,
            # max sum from root with branching, or keep current max sum
            max_sum[0] = max(max_root_path_nb, root.val+left+right, max_sum[0])

            return max_root_path_nb

        maxPathSumHelper(root)

        return max_sum[0]