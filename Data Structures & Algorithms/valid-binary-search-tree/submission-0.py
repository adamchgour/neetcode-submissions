# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,min_so_far,max_so_far):
            ''' less than the min '''
            if node is None:
                return True
            if node.val <= min_so_far or node.val >= max_so_far :
                return False
            min_so_far = min(node.val,min_so_far)
            max_so_far = max(node.val,max_so_far)

            return dfs(node.left,min_so_far,node.val) and dfs(node.right,node.val,max_so_far)

        return dfs(root,float("-inf"),float("inf"))
    