"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        q=[root]
        while q:
            for _ in range(len(q)):
                curr=q.pop(0)
                
                if q:
                    curr.next = q[0]
                    
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
                    
                    
            curr.next=None
            
        return root
                
        