# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow and fast ptr to find the mid point
        # then reverse the second half and interleave

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half

        prev = None
        curr = slow.next
        slow.next = None

        # remember in python that tuple style swapping is pretty cool
        # especially for LL work -- don't need to worry about temps
        # because the RHS is fully evaluated before assignments

        while curr:
            # temp = curr.next
            # curr.next = prev
            # prev = curr
            # curr = temp

            curr.next, prev, curr = prev, curr, curr.next
        
        # interleave
        first, second = head, prev

        while second:
            # first_next = first.next
            # first.next = second
            # first = first_next

            first.next, first = second, first.next

            # second_next = second.next
            # second.next = first
            # second = second_next

            second.next, second = first, second.next
            
            

