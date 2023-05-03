class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        self.checks(candidates,target,[],res)
        return res
        
        
    def checks(self,nums,target,path,res):
        if target<0:
            return 
        if target==0:
            res.append(path)
            return
        for i in range(len(nums)):
            self.checks(nums[i:],target-nums[i],path+[nums[i]],res)
        
        