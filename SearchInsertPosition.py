class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=len(nums)
        i=0
        while(i<l):
            if nums[i]==target:
                return i
            if target<nums[i]:
                return i
            i+=1
        return i
        
        