class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if "-" in x:
            x=x.replace("-","")
            x=x+"-"
            x=int(x[::-1])
            return x if -(2**31)-1 < x < 2**31 else 0
        x=int(x[::-1])
        return x if -(2**31)-1 < x < 2**31 else 0
        
#####alt

class Solution:
    def reverse(self, x: int) -> int:
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0