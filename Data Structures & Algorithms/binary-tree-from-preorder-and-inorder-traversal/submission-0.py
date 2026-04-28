# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node_to_in = {v: i for i,v in enumerate(inorder)}
        self.preorder_ptr = 0

        def buildTreeHelper(l, r):
            if l > r:
                return None

            root_val = preorder[self.preorder_ptr]
            self.preorder_ptr += 1
            
            node = TreeNode(root_val)

            root_index = node_to_in[root_val]
            node.left = buildTreeHelper(l, root_index-1)
            node.right = buildTreeHelper(root_index+1, r)

            return node
        
        return buildTreeHelper(0, len(inorder)-1)
                
