# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res,stack=[],[]
        current=root
        while True:
            while current:
                stack.append(current)
                res.append(current.val)
                current=current.right
            if(len(stack)==0):
                return res[::-1]
            node=stack[-1]
            stack.pop(len(stack)-1)
            
            current=node.left
        return res[::-1]

###proper method:
class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        res,stack=[],[[root,0]]
        while stack:
            node=stack[-1]
            stack.pop()
            
            if node[1]==0:
                current=node[0]
                stack.append([current,1])
                if current.right :
                    stack.append([current.right,0])
                if current.left :
                    stack.append([current.left,0])
            else:
                if node[0].val!=0:
                    res.append(node[0].val)
        return res

