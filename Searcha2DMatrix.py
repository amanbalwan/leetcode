class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False 
        
        r=len(matrix)
        c=len(matrix[0])
        
        first=0
        last=(r*c)-1
        
        while first<=last:
            mid=(first+last)//2
            num=matrix[mid//c][mid%c]
            
            if num==target:
                return True
            elif num<target:
                first=mid+1
            else:
                last=mid-1
                
        return False
                
        
                
                
        