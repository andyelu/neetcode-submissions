# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow and fast ptr to find the mid point
        # then reverse the second half and interleave

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # slow is now at the midpoint (pointing to last element
        # of the first half of the list)

        prev = None
        curr_r_half = slow.next
        slow.next = None

        while curr_r_half:
            temp = curr_r_half.next
            curr_r_half.next = prev
            prev = curr_r_half
            curr_r_half = temp
        
        curr = head

        while prev != None:
            next_curr = curr.next
            next_prev = prev.next

            curr.next = prev
            curr.next.next = next_curr
            curr = next_curr

            prev = next_prev