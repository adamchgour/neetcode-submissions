# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def bfs(root):
            if root is None:
                return []
            result = []
            q = deque([root]) 
            
            while q:
                res = []
                for i in range(len(q)):
                    curr = q.pop()
                    if curr.left:
                        q.appendleft(curr.left)
                    if curr.right:
                        q.appendleft(curr.right)
                    res.append(curr.val)
                result.append(res)
            return result
            
        result = bfs(root)

        for i in range(len(result)):
            ans.append(result[i][-1])
        
        return ans