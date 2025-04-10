class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(index, candidates, targ, res, ans):
            if index == len(candidates):
                if targ == 0:
                    res.append(ans[:])
                return

            if candidates[index] <= targ:
                ans.append(candidates[index])
                backtrack(index, candidates, targ - candidates[index],res,ans)
                ans.pop()
            
            backtrack(index+1,candidates, targ, res, ans) 
        
        res = []
        backtrack(0, candidates, target, res, [])

        return res