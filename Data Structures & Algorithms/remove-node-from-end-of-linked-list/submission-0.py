# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        norm = dummy
        shift = head

        for i in range(n-1):
            shift = shift.next
        
        while shift :
            shift = shift.next
            if shift:
                norm = norm.next

        norm.next = norm.next.next

        return dummy.next