class Solution:
    def titleToNumber(self, c: str) -> int:
        a=0
        l=len(c)
        for n in range(l):
            a+=(ord(c[n])-64)*pow(26,l-n-1)
        return a
        
        
        