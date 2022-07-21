# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        if n == 0:
            return None
    
        l = 1
    
        while l<n and preorder[l] < preorder[0]:
            l += 1
    
        root = TreeNode(preorder[0])
        root.left = self.bstFromPreorder(preorder[1:l])
        root.right = self.bstFromPreorder(preorder[l:n])
    
        return root
        