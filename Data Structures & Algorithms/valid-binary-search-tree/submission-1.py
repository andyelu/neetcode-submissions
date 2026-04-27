# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))

    def isValidBSTHelper(self, root: Optional[TreeNode], min_val: Integer, max_val: Integer) -> bool:
        if not root:
            return True

        if min_val >= root.val or root.val >= max_val:
            return False

        return self.isValidBSTHelper(root.left, min_val, root.val) and self.isValidBSTHelper(root.right, root.val, max_val)
