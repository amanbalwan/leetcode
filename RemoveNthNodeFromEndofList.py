# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return None
        current=head
        current1=head
        prev=current
        Final=0
        while current1:
            Final+=1
            current1=current1.next
        v=0
        if Final-n==0:
            head=current.next
            return head
        while current:
            
            if v==Final-n:
                prev.next=current.next
                current=current.next
                return head
            else:
              
                prev=current
                current=current.next
            v+=1
        return head
                
           
        