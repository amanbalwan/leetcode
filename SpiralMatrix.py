class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        
        top=0
        bottom=m-1
        left=0
        right=n-1
        
        res=[]
        
        while top<=bottom and left<=right:
            for col in range(left,right+1):
                res.append(matrix[left][col])
            top+=1
            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            right-=1
            for col in range(right,left-1,-1):
                res.append(matrix[bottom][col])
            bottom-=1
            for row in range(bottom,top-1,-1):
                res.append(matrix[row][left])
            left+=1
            
        return res[:m*n]
                
            
                
        