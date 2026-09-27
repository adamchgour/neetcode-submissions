# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q:
            return False
        elif q is None and p :
            return False
        elif q is None and p is None :
            return True

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and q.val == p.val 