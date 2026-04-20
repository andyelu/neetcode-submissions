# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# import to recognize that we don't need a visited set for this question
# but instead we can utilize slow and faster pointers for LL
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next

            if (fast == slow):
                return True
        return False
        