# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        current=head
        while current is not None:
            if head is None:
                return []
            if head.val==val:
                head=current.next
                prev=current
                current=current.next
            elif current.val==val:
                prev.next=current.next
                current=current.next
            else:
                prev=current
                current=current.next
                
                
            
            
        return head
                
                
            