# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def getans(root, ans):
            if root is None:
                return 0
            
            
            
            left = getans(root.left, ans)
                
            
            right = getans(root.right, ans)
                
            return 1+max(left, right)
            
        
        
        
        
        return getans(root, 0)
    
    
    
        
        