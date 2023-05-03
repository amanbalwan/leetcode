class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        maxpos=0
        i=0
        while i<=maxpos:
            maxpos=max(maxpos,i+nums[i])
            if maxpos>=n-1:
                return True
            i+=1
        return False
            
        