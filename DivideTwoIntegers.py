class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend>0) is (divisor>0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        count=0
        
        while dividend>=divisor:
            cdivisor,num=divisor,1
            while dividend>=cdivisor:
                dividend-=cdivisor
                count+=num
                
                num<<=1
                cdivisor<<=1
                
        if not sign:
            count=-count
        return min(max(-2147483648,count),2147483647)
                
                
        
        
        
            
        