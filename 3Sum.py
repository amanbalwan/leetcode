class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l += 1; r -= 1
            
        return res


###using while loop
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        i=0
        while i < len(nums)-2:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l += 1; r -= 1
            i+=1
        return res


###works for small cases only my very own
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        l=len(nums)
        i=0
        sum=set()
        
        while i<l:
            j=i+1
            while j<l:
                k=j+1
                while k<l:
                    if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                            sum.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                            
                    k+=1
                j+=1
            i+=1
        return sum
    
