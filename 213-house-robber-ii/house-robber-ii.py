class Solution:
    def rob0(self, nums: List[int]) -> int:
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
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob0(nums[0:n-1]), self.rob0(nums[1:]))