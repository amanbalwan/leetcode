class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       
        def search(lo,hi):
            if nums[lo]==target==nums[hi]:
                return [lo,hi]
            if nums[lo]<=target<=nums[hi]:
                m=(lo+hi)//2
                l,r=search(lo,m),search(m+1,hi)
                return max(l,r) if -1 in l+r else [l[0],r[1]]
            
            return [-1,-1]
        
        return search(0,len(nums)-1) if nums!=[] else [-1,-1]