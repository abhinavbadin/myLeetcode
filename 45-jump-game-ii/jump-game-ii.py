class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        n_jumps = 0
        l,r = 0,0
        
        while r < n-1:
            maxIndex = 0 
            for index in range(l,r+1):
                maxIndex = max(maxIndex, index+nums[index])
            l = r+1
            r = maxIndex
            n_jumps+=1
        return n_jumps