class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        l,r=0,len(nums)-1
        
        
        while l<=r:
            
            m=(l+r)//2
            
            if target==nums[m]:
                return True
            while l<m and nums[l]==nums[m]:
                l+=1
            while r>m and nums[r]==nums[m]:
                r-=1
            if nums[m]>=nums[l] :
                if target<nums[m] and target>=nums[l]:
                    r=m-1
                else:
                    l=m+1
            else:
                if target>nums[m] and target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
                
                
                
            
        return False