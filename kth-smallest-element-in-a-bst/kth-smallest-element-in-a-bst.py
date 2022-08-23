# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def getans(root, inorder):
            if not root:
                return root
            
            getans(root.left, inorder)
            inorder.append(root.val)
            getans(root.right, inorder)
        
        
        inorder=[]
        getans(root, inorder)
        return inorder[k-1]
        