class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def climbingCost(index,dp):
            if index == 0 or index == 1:
                return cost[index]
            
            if dp[index] != -1:
                return dp[index]
            
            take = climbingCost(index-2,dp)
            noTake = climbingCost(index-1,dp)

            dp[index] = cost[index] + min(take,noTake)

            return dp[index]
        
        n = len(cost)
        dp = [-1] * (n+1)
        return min(climbingCost(n-1,dp),climbingCost(n-2,dp)) 