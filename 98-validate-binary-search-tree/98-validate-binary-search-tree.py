# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
    
        def check(root, mini, maxi):
            if root==None:
                return True
            if mini!=None and root.val <= mini.val:
                return False
            if maxi!=None and root.val >= maxi.val:
                return False
            
            return check(root.left, mini, root) and check(root.right, root, maxi)
            
        return check(root, None, None)
    
    
    
        
        