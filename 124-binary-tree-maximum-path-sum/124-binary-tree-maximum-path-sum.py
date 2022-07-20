# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxi = float("-inf")
        def getans(root):
            
            if root is None:
                return 0
            
            lh = max(0, getans(root.left))
            rh = max(0, getans(root.right))
            self.maxi = max(self.maxi, lh+rh+root.val)
            
            return root.val + max(lh, rh)
        
        
        
        getans(root)
        return self.maxi
        