# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def getans(root, maxi):
            if not root:
                return 0
            
            count=0
            if root.val >= maxi:
                count+=1
                maxi = root.val
                
            count+=getans(root.left, maxi)
            count+=getans(root.right, maxi)
            
            return count
        
       
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        good=1
        good+=getans(root.left, root.val)
        good+=getans(root.right, root.val)
        
        return good