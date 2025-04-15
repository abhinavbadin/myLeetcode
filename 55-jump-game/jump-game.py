class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxIndex = 0 

        for i in range(0,n):
            if i > maxIndex: #this means it cant touch that index so how come it can go there 
                return False
            maxIndex = max(maxIndex,i+nums[i])
        return True 