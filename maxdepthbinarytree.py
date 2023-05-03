# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         k=0
#         def dep(k,l,r):
            
            
#             if not l and r:
#                 k+=1
#                 return dep(k,r.left,r.right)
#             elif not r and l:
#                 k+=1
#                 return dep(k,l.left,l.right)
#             elif l and r:
#                 k+=1
#                 return dep(k,l.left,r.right)
#             elif not l and not r:
#                 return k
#             else:
#                 return k
                
                
            
#         if root and (root.left or root.right):
#              return dep(k+1,root.left,root.right)

#         elif root:
#             return k+1
    
#         else:
#             return k

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
       
            if not root:
                return 0
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
            
       