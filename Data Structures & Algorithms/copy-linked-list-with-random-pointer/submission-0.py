"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head  
        corr = {None : None} # corresponding table
        
        # first loop

        while temp:
            corr[temp] = Node(temp.val)
            temp = temp.next
        
        # second loop
        temp = head

        while temp :
            corr[temp].next = corr[temp.next]
            corr[temp].random = corr[temp.random]

            temp = temp.next

        return corr[head]