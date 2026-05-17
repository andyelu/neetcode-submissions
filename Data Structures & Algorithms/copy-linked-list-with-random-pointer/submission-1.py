"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        res_ptr = dummy

        old_to_new = {}
        prev_new = None
        curr = head

        # create the new nodes and establish old to new mapping
        while curr:
            new = Node(curr.val)

            if prev_new:
                prev_new.next = new
            prev_new = new

            old_to_new[curr] = new
            curr = curr.next

        curr = head
        while curr:
            res_ptr.next = old_to_new[curr]
            res_ptr = res_ptr.next
            if curr.random:
                res_ptr.random = old_to_new[curr.random]
            else:
                res_ptr.random = None
            curr = curr.next

        return dummy.next
        

    