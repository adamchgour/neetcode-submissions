# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head : fast = head.next
        else : return False

        while fast and fast.next :
            if head == fast:
                return True
            
            fast = (fast.next).next
            head = head.next
            
        return False
