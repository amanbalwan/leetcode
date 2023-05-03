class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r={}
        for num in nums:
           
                
            if num not in r:
                r[num]=0
            else:
                r[num]+=1
        return max(r,key=r.get)
        
###Alt@@@@@@@

class Solution:
    def majorityElement(self, num: List[int]) -> int:
        r={}
        i=0
        l=len(num)
        while i<l:
           
                
            if num[i] not in r:
                r[num[i]]=0
                i+=1
            else:
                r[num[i]]+=1
                i+=1
        return max(r,key=r.get)
        