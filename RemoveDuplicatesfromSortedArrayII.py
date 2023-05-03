class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return nums
        i=0
        while True:
            try:
                if nums[i]==nums[i+1]:
                    j=i+2
                    while True and j<len(nums):
                        if nums[j]==nums[i]:
                            nums.pop(j)

                        else:
                            break
                i+=1
            except:
                return 
        