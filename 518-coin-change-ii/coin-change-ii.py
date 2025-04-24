class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def func(ind,target, arr, dp):
            if ind == 0:
                if target % arr[ind] == 0:
                    return 1 
                else:
                    return 0
            
            if dp[ind][target] != -1:
                return dp[ind][target]
            
            notTake = func(ind-1, target, arr, dp)
            take = 0
            if arr[ind] <= target:
                take = func(ind, target - arr[ind], arr, dp)
            dp[ind][target] = take + notTake
            return dp[ind][target]
        
        
        n = len(coins)
        dp = [[-1 for i in range(amount+1)] for j in range(n)]
        return func(n-1, amount, coins, dp)