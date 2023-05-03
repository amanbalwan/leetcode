# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res,stack=[],[]
        current=root
        while True:
            while current:
                stack.append(current)
                current=current.left
            if(len(stack)==0):
                return res
            node=stack[-1]
            stack.pop(len(stack)-1)
            if(node.val!=None):
                res.append(node.val)
            current=node.right
        return res