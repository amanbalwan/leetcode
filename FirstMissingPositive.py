class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1 if nums[0]>1 or nums[0]<1 else 2
        
        s=[]
        
        for i in range(len(nums)): 
            if nums[i]>0 and nums[i]<=len(nums) :
                s.append(nums[i])
        
        s=set(s)
        s=list(s)
        s.sort()
        count=1
        i=0
        while i<len(s):
            if count<s[i]:
                return count
            else:
                count+=1
        
            i+=1
        return count