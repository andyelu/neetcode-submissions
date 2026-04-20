# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        counter = 0

        def inorderHelper(curr):
            nonlocal res, counter
            if not curr or res is not None:
                return

            inorderHelper(curr.left)

            counter += 1
            if (counter == k):
                res = curr
                return

            inorderHelper(curr.right)

        inorderHelper(root)

        return res.val
            

