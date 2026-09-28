# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        def bfs(root):
            if root is None:
                return []
            result = []
            q = deque([root]) 
            
            while q:
                for i in range(len(q)):
                    curr = q.pop()
                    if curr.left:
                        q.appendleft(curr.left)
                    if curr.right:
                        q.appendleft(curr.right)
                self.ans.append(curr.val)
            return result
            
        result = bfs(root)
        
        return self.ans