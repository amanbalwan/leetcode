class Solution:
    def maxProfit(self, price: List[int]) -> int:
        n=len(price)
        
        l=0
        r=1
        m=0
        while(r<n):
            cp=price[r]-price[l]
            if price[r]>price[l]:
                m=max(cp,m)
            else:
                l=r
            r+=1
        return m
            
            
         
            
            
        