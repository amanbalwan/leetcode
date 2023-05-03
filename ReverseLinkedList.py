# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def newn(node,prev=None):
            
            if not node:
                return prev
            
            
            n=node.next
            node.next=prev
                  
            return newn(n,node)
        if not head:
            return None
        
        return newn(head)
        
        