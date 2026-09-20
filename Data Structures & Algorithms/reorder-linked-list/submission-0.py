# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the midpoint
        slow = head
        fast = head

        while fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        slow.next = None

        # Reverse the "Right linked List"

        prev = None
        curr = right

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        right = prev
        # Merge the two lists

        left = head

        while right:
            next_left = left.next
            next_right = right.next

            left.next = right
            right.next = next_left

            left = next_left
            right = next_right

        if head is None:
            return
        