# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def getans(left, right):
            
            ans=[]
            if left>right:
                return [None]
            
            for i in range(left, right+1):
                leftnode = getans(left, i-1)
                rightnode = getans(i+1, right)
                
                for x in leftnode:
                    for y in rightnode:
                        newnode = TreeNode(i)
                        newnode.left = x
                        newnode.right = y
                        ans.append(newnode)
                        
                        
            return ans
        
        
        
        
        
        
        
        
        return getans(1, n)