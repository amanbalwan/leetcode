##short but not needed
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1=int(num1)
        num2=int(num2)
        return str(num1*num2)

###actual
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product=[0]*(len(num1)+len(num2))
        pos=len(product)-1
        
        for n1 in reversed(num1):
            temp=pos
            for n2 in reversed(num2):
                product[temp]+=int(n1)*int(n2)
                product[temp-1]+=product[temp]//10
                product[temp]%=10
                temp-=1
            pos-=1
        
        pt=0
        while pt<len(product)-1 and product[pt]==0:
            pt+=1
        return "".join(map(str,product[pt:]))
                       
