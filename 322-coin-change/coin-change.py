class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def func(ind,target,arr,dp):
            if ind == 0:
                if target % arr[ind] == 0:
                    return target // arr[ind]
                else:
                    return float('inf')
            
            if dp[ind][target] != -1:
                return dp[ind][target]
            
            notTake = 0 + func(ind-1, target, arr, dp)
            take = float('inf')
            if arr[ind] <= target:
                take = 1 + func(ind, target - arr[ind], arr, dp)
            
            dp[ind][target] = min(take, notTake)
            return dp[ind][target]
        
        n = len(coins)
        dp = [[-1 for i in range(amount+1)] for j in range(n)]
        ans = func(n-1, amount, coins,dp)

        if ans >= float('inf'):
            return -1
        else:
            return ans
 