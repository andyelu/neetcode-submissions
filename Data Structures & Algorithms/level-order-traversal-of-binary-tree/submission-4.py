from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # For this question, I obviously knew that I needed to use a BFS traversal.
        # But how do we know when our level list ends. Well at each iteration in our
        # outer while loop, we can assume that the queue start here contains all 
        # level nodes without any popped yet. So the current length of the queue will
        # be the total number of nodes in the level. So our inner loop in the queue
        # will popleft each node, add the value to the res list, and add children.

        # we only visit each node once, so this is O(n) runtime. We store one list
        # element for each node, so space is also O(n)

        res = []
        if not root:
            return res

        q = deque()

        q.append(root)

        while q:
            level_total = len(q)
            level_list = []

            for i in range(level_total):
                curr = q.popleft()

                level_list.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            res.append(level_list)

        return res




