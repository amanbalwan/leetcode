class Treenode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def insert(temp,val):
    que=[]
    que.append(temp)
    while(len(que)):
        temp=que[0]
        que.pop(0)
        if(not temp.left):
            temp.left=Treenode(val)
            break
        else:
            que.append(temp.left)
        if(not temp.right):
            temp.right=Treenode(val)
            break
        else:
            que.append(temp.right)
            
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p and q:
            return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return p is q
        
a=Solution()
