"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans=[]
        queue=deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if node:
                if level==len(ans):
                    ans.append([])
                    
                #if node:
                ans[level].append(node.val)
                #if node:
                for c in node.children:
                    queue.append((c, level+1))
            #if node.right:
            #    queue.append((node.right, level+1))
                
        if len(ans)==0:
            return []
        return ans
    
    
#         d = dict()
#         if not root:
#             return []
        
        
#         q = [[root,1]]
        
#         while q:
#             poped,l = q.pop(0)
            
#             if l in d:
#                 d[l].append(poped.val)
#             else:
#                 d[l] = [poped.val]
                
#             for c in poped.children:
#                 if c:
#                     q.append([c,l+1])
                
#         return list(d.values())
        