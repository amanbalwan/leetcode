class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        number=[i+1 for i in range(n)]
        answer=""
        
        for nt in range(n,0,-1):
            d=(k-1)//factorial(nt-1)
            k-=d*factorial(nt-1)
            answer += str(number[d])
            number.remove(number[d])
           
        return answer
       