class Solution:
    def convertToTitle(self, num: int) -> str:
        d=ord('A')
        result=''
        while num>0:
            y=(num-1)%26
            num=(num-1)//26
            result+=chr(y+d)
        return result[::-1]
            
        