class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum = float("-inf")
        n = len(nums)
        j,summ = 0,0

        while j < n:
            summ = max(summ+nums[j],nums[j])
            msum = max(summ,msum)
            j+=1
        
        return msum