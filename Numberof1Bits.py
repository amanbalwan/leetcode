class Solution:
    def hammingWeight(self, n: int) -> int:
        i=0
        k=0
        while i<32:
            if n&1==1:
                k+=1
            n>>=1   
            i+=1
        return k
        
        