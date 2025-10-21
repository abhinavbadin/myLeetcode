class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        
        nums.sort()
        
        def backtrack(index,path,target):
            if target == 0:
                res.append(path[:])
                return 
            
            if target < 0:
                return

            for i in range(index,len(nums)):

                if i > index and nums[i] == nums[i-1]:
                    continue 
                
                if nums[i] > target:
                    break
                
                path.append(nums[i])
                backtrack(i+1,path,target - nums[i])
                path.pop()
        
        res = []
        backtrack(0,[],target)
        return res