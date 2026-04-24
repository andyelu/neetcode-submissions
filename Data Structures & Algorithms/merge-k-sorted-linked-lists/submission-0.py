# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        res_ptr = dummy

        while True:
            min_val = float("inf")
            min_node_i = None
            for i,node in enumerate(lists):
                if node and min_val > node.val:
                    min_val = node.val
                    min_node_i = i
            
            # break if all list indices point to nothing
            if min_node_i is None:
                break

            # add to our result
            res_ptr.next = lists[min_node_i]
            res_ptr = res_ptr.next
            
            # update the node that the list index points to
            lists[min_node_i] = lists[min_node_i].next

        return dummy.next