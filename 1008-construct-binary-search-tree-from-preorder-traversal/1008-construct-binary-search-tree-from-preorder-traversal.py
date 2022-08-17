# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def getans(inorder, preorder):
            if not inorder or not preorder:
                return None
            
            root=TreeNode(preorder[0])
            mid = inorder.index(root.val)
            
            root.left = getans(inorder[:mid], preorder[1:mid+1])
            root.right = getans(inorder[mid+1:], preorder[mid+1:])
            
            return root
        
        
        
        
        
        
        
        
        
        inorder = preorder.copy()
        inorder.sort()
        #print(inorder)
        return getans(inorder, preorder)
    
    
        