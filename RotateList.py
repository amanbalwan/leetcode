# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        lastelement=head
        length=1
        
        while(lastelement.next):
            lastelement=lastelement.next
            length+=1
            
        k=k%length
        
        lastelement.next=head
        
        tempnode=head
        
        for _ in range(length-k-1):
            tempnode=tempnode.next
        
        answer=tempnode.next
        tempnode.next=None
        
        return answer