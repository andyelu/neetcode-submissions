# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # with a dummy node, we don't need to worry
                            # about, is the result head None or not? Just
                            # makes the code cleaner
        res_ptr = dummy

        while list1 and list2:
            if (list1.val < list2.val):
                res_ptr.next = list1
                list1 = list1.next
            else:
                res_ptr.next = list2
                list2 = list2.next
            res_ptr = res_ptr.next

        if (list1):
            res_ptr.next = list1
        if (list2):
            res_ptr.next = list2

        return dummy.next
            

        
            
            
