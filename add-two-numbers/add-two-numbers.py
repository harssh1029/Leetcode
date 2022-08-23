# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lone = l1
        ltwo = l2
        carry=0
        ans = ListNode(None)
        head=ans
        while l1 and l2:
            summ = l1.val + l2.val + carry
            
            ele = summ%10
            carry = summ//10
            #print(summ, carry)
            ans.next = ListNode(ele)
            ans=ans.next
            l1=l1.next
            l2=l2.next
            
        while l1:
            summ = l1.val + carry
            ele=summ%10
            carry=summ//10
            ans.next= ListNode(ele)
            ans=ans.next
            l1=l1.next
            
        while l2:
            summ = l2.val + carry
            ele=summ%10
            carry=summ//10
            ans.next= ListNode(ele)
            ans=ans.next
            l2=l2.next
        
        if carry!=0:
            ans.next = ListNode(carry)
            
        return head.next
            
            
        