class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[0] = nums[0]

        for i in range(1,len(nums)):
            take = nums[i]
            if i > 1:
                take += dp[i-2]
            notake = 0 + dp[i-1]
            dp[i] = max(take,notake)
        
        return dp[len(nums)-1]