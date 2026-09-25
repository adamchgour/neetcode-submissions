# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        dummy = ListNode()
        curr = dummy 

        for i in range(len(lists)):
            if lists[i]:  # attention aux listes vides
                heapq.heappush(
                    min_heap,
                    (lists[i].val, i, lists[i])
                )

        while min_heap:
            value, i, node = heapq.heappop(min_heap)
            if node.next:
                heapq.heappush(min_heap,(node.next.val,i,node.next))
            curr.next = node
            curr = curr.next
            
        return dummy.next