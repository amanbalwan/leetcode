##compare one by one
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return []
        compare = [list.val if list else float("inf") for list in lists]
        # print(compare)
        dummy = ListNode(0)
        node = dummy
        while min(compare) < float("inf"):
            minC = min(compare)
            idx = compare.index(minC)
            node.next = ListNode(minC)
            node = node.next
            lists[idx] = lists[idx].next
            compare[idx] = lists[idx].val if lists[idx] else float("inf")
            # print(compare)
        return dummy.next

#merge sort
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        m=len(lists)//2
        l,r=self.mergeKLists(lists[:m]),self.mergeKLists(lists[m:])
        return self.merge(l,r)
    
    def merge(self,l,r):
        dummy=p=ListNode()
        while l and r:
            if l.val<r.val:
                p.next=l
                l=l.next
            else:
                p.next=r
                r=r.next
            p=p.next
        p.next= l or r
        return dummy.next
           
            
                
        