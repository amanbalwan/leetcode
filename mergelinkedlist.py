def mergeTwoLists(self, list1, list2):
    dummynode=ListNode(0)
    tail=dummynode
    l1=list1
    l2=list2
    while True:
        
        if l1 is None:
            tail.next=l2
            break
        if l2 is None:
            tail.next=l1
            break
        if l2.val>=l1.val:
            tail.next=l1
            l1=l1.next
        elif l1.val>l2.val:
            tail.next=l2
            l2=l2.next
        print(tail.val)
        tail=tail.next
    return dummynode.next
                