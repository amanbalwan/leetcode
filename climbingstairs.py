class Solution:
    def climbStairs(self, n: int) -> int:
        a=b=1
        for _ in range(n):
            a,b=b,a+b
            
        return a

s=Solution()
k=s.climbStairs(3)
print(k)