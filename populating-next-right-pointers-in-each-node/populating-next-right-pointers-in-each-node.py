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
        
        black = root
        while black and black.left:
            n=black
            
            while (True):
                n.left.next=n.right
                if not n.next:
                    break
                    
                n.right.next=n.next.left
                n=n.next
                
                
            black=black.left
            
        return root