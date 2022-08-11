# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def gettotal(root):
            if not root:
                return 0
            
            left=gettotal(root.left)
            right=gettotal(root.right)
            return (root.val+left+right)
        
        
        def getans(root, totalsum,ans):
            if not root:
                return 0
            
            subtree=0
            subtree+=getans(root.left, totalsum, self.ans)
            subtree+=getans(root.right, totalsum, self.ans)
            subtree+=root.val
            if subtree*(totalsum-subtree)>self.ans:
                self.ans=subtree*(totalsum-subtree)
            
            return subtree
        
        
        totalsum = gettotal(root)
        
        getans(root, totalsum, self.ans)
        return self.ans%1000000007
        
        
        