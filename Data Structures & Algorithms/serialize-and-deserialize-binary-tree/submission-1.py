from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""

        if not root:
            return res

        queue = deque([root])
        added_non_null = True
        first_val = True

        while added_non_null and queue:
            curr_q_len = len(queue)
            added_non_null = False

            for _ in range(curr_q_len):
                curr = queue.popleft()

                if not first_val:
                    res += ","
                else:
                    first_val = False

                if curr:
                    res += str(curr.val)
                else:
                    res += "null"

                # enqueue the children, including nulls
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    if not added_non_null and (curr.left or curr.right):
                        added_non_null = True

        return res
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        node_vals = data.split(",")
        node_count = len(node_vals)

        res = TreeNode(node_vals[0])
        node_val_ptr = 0

        leaf_queue = deque([res])

        while leaf_queue:
            leaf_q_len = len(leaf_queue)
            for _ in range(leaf_q_len):
                curr = leaf_queue.popleft()
                if not curr:
                    continue
                
                if node_val_ptr + 2 < node_count:
                    left = TreeNode(node_vals[node_val_ptr+1])
                    right = TreeNode(node_vals[node_val_ptr+2])
                    curr.left = left
                    curr.right = right
                    leaf_queue.append(left)
                    leaf_queue.append(right)

                    node_val_ptr += 2

        return res

