# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        # Both starts at the head
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next        # moves slow pointer by one
            fast = fast.next.next   # moves fast pointer by two

            if slow == fast:
                return True         # there's a cycle
        
        return False                # no cycle if fast reaches end
