# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def depth(root):
            nonlocal diameter
            if root is None:
                return 0

            diameter = max(diameter,depth(root.left) + depth(root.right))
            return 1 + max(depth(root.left),depth(root.right))
        depth(root)
        
        return diameter