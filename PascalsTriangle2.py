class Solution:
    def getRow(self, num: int) -> List[int]:
        res=[[1]] 
        for i in range(num):
            res+=[list(map(lambda x,y: x+y , res[-1]+[0],[0]+res[-1]))]
        return res[num]
        