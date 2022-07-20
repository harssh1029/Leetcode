# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans=[]
        if not root:
            return ans
        
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if len(ans)==level:
                ans.append([])
                
            ans[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
                
            if node.right:
                queue.append((node.right, level+1))
                
        for x, y in enumerate(ans):
            if x%2!=0:
                y.reverse()
                
        return ans
            
                
            