# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempone = headA
        temptwo = headB
        while tempone!=temptwo:
            if not tempone:
                tempone=headB
            else:
                tempone=tempone.next
                
            if not temptwo:
                temptwo=headA
            else:
                temptwo=temptwo.next
                
        return tempone
                
            