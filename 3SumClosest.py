##TLE error
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result=nums[0]+nums[1]+nums[2]
        
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,len(nums)-1
            while j< k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==target:
                    return sum
                
                if abs(sum-target)<abs(result-target):
                    result=sum
                    
                if sum<target:
                    j+=1
                else :
                    k-=1
                
                
                    
            
            
        return result
    ##tle error with while loop
     def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result=nums[0]+nums[1]+nums[2]
        i=0
        while i< (len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j,k=i+1,len(nums)-1
            while j< k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==target:
                    return sum
                
                if abs(sum-target)<abs(result-target):
                    result=sum
                    
                if sum<target:
                    j+=1
                else :
                    k-=1
                while j<k and nums[j]==nums[j+1]:
                        j+=1
                while j<k and nums[j]==nums[k-1]:
                        k-=1
                
                    
            i+=1
            
        return result
        
##noTLE
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result=nums[0]+nums[1]+nums[2]
        i=0
        if (x := sum(nums[:3])) >= target:
            return x
        if (x := sum(nums[-3:])) <= target:
            return x
        while i< (len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j,k=i+1,len(nums)-1
            while j< k:
                sum1=nums[i]+nums[j]+nums[k]
                if sum1==target:
                    return sum1
                
                if abs(sum1-target)<abs(result-target):
                    result=sum1
                    
                if sum1<target:
                    j+=1
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                else:
                    k-=1
                    while j<k and nums[j]==nums[k-1]:
                        k-=1
                
                    
               
                
                
          
            i+=1
            
        return result
        
        