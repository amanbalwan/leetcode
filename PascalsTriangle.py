class Solution:
    def generate(self, num: int) -> List[List[int]]:
        res=[[1]] 
        for i in range(num-1):
            res+=[list(map(lambda x,y: x+y , res[-1]+[0],[0]+res[-1]))]
        return res
                
            
               
            
        