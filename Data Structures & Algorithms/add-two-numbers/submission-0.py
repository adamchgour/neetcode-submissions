# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,l1)
        stored = 0

        while l1 :
            s = l1.val + (l2.val if l2 else 0) + stored
            stored = s // 10
            l1.val = s%10

            if l2:
                l2 = l2.next
            
            if (not l1.next) and (l2 or stored != 0):
                l1.next = ListNode(0)
            l1 = l1.next
        
        return dummy.next


