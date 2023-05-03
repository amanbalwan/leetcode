# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,res=[],[]
        current= root
        while True:
            while current:
                stack.append(current)
                res.append(current.val)
                current=current.left
            if len(stack)==0:
                return res
            node=stack[-1]
            stack.pop(-1)
            current=node.right
        return res
            
#### or
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.help(res,root)
        return res
    def help(self,res,root):
        if root:
            res.append(root.val)
            self.help(res,root.left)
            self.help(res,root.right)