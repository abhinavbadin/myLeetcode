class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, prev2 = nums[0], 0 

        for i in range(1,len(nums)):
            take = nums[i]
            if i > 1:
                take += prev2
            notake = 0 + prev

            curr = max(take,notake)
            
            prev2 = prev
            prev = curr
        
        return prev