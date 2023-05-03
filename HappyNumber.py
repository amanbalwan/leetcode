class Solution:
    def isHappy(self, n: int) -> bool:
            s=set()
            while(n!=1):
                a=0
                while n is not 0:
                    a+=pow((n%10),2)
                    n//=10
                n=a
                if n not in s:
                    s.add(n)
                else:return False
                    
                    
                

            return True
       