class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(l,r,target,N,result,results):
            if r-l+1<N or N<2 or target<nums[l]*N or target>nums[r]*N:
                return
            if N==2:
                
                while l<r:
                    sum=nums[l]+nums[r]
                    if sum==target:
                        results.append(result+[nums[l],nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l+=1
                        r-=1
                        
                    elif sum>target:
                        r-=1
                    else:
                        
                    
            else:
                i=l
                while l<=i and i<r+1:
                    if i==l or (i>l and nums[i]!=nums[i-1]):
                        
                        findNsum(i+1,r,target-nums[i],N-1,result+[nums[i]],results)
                    i+=1
            
                    
        nums.sort()
        results=[]
        findNsum(0,len(nums)-1,target,4,[],results)
        return results