# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        even, odd = head.next, head
        even_start = even
		# group the odds and evens seperately
        while odd.next and even.next:
            odd.next, odd = odd.next.next, odd.next.next
            even.next, even = even.next.next, even.next.next
        # combine the groups    
        odd.next = even_start 

        return head 
        