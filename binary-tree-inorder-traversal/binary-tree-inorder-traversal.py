# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def getans(root, ans):
            if not root:
                return
            
            getans(root.left, ans)
            ans.append(root.val)
            getans(root.right, ans)
        
        
        
        ans=[]
        getans(root, ans)
        return ans
        