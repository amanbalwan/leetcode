class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for i in range(32):
            result=(result<<1)+(n&1)
            n>>=1
        return result

c=Solution()
print(c.reverseBits(0b10100101000001111010011100))