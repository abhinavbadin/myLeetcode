class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        def backtrack(index,path,target):
            if target == 0:
                res.append(path[:])
                return
            
            if index == len(nums) or target < 0:
                return
            
            backtrack(index+1,path,target)
            
            # target -=nums[index] not recommended
            path.append(nums[index])
            backtrack(index,path,target-nums[index])
            path.pop()
        
        res = []
        backtrack(0,[],target)
        return res