class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        curr_index = 0

        # we will advance curr to the nth node and keep track of the node n positions back
        past_node = head

        for i in range(n):
            curr = curr.next
            curr_index += 1

        # now advance both pointers until curr is null
        if not curr:
            return head.next

        while curr.next:
            curr = curr.next
            curr_index += 1
            past_node = past_node.next

        # past_node.next is now the nth node from end
        past_node.next = past_node.next.next
        return head