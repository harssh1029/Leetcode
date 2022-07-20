# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxi=-1
        
        def getans(root):
            if root is None:
                return 0
            
            lh = getans(root.left)
            rh = getans(root.right)
            
            self.maxi = max(self.maxi, lh+rh)
            return 1+max(lh, rh)
        
        
        
        
        getans(root)
        return self.maxi
        