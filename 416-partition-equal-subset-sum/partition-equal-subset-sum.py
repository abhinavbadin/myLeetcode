class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subsetSum(n,k,arr):
            prev = [False] * (k+1)
            prev[0] = True 
            
            if arr[0] < k:
                prev[arr[0]] = True

            for ind in range(1,n):
                curr = [False] * (k+1)
                curr[0] = True

                for target in range(1,k+1):
                    notTake = prev[target]

                    take = False
                    if arr[ind] <= target:
                        take = prev[target-arr[ind]]
                    curr[target] = take or notTake  
                prev = curr
            return prev[k]

        totSum = 0 
        for i in range(0,len(nums)):
            totSum += nums[i]
        
        if (totSum % 2):
            return False
        
        target = totSum // 2
        
        return subsetSum(len(nums),target,nums)


