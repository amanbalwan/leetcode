class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        self.checks(candidates,target,0,[],res)
        return res
        
        
    def checks(self,nums,target,idx,path,res):
        if target<0:
            return 
        if target==0:
            res.append(path)
            return
        for i in range(idx,len(nums)):
            if i>idx and nums[i]==nums[i-1] :
                continue
            self.checks(nums,target-nums[i],i+1,path+[nums[i]],res)
        
        