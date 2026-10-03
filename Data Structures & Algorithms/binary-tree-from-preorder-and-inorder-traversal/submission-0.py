# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ''' The root of the node is easy to find in the preorder traversal '''
        h = {}
        self.pre_index = 0

        for i in range(len(inorder)) :
            h[inorder[i]] = i
        
        def build(left, right):

            if left > right:
                return None
            
            value = preorder[self.pre_index]
            root = TreeNode(value)
            self.pre_index += 1

            mid = h[value]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0,len(preorder)-1)
        
                
            