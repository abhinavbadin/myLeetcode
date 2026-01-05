class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # l,r = 0,1
        # while r<len(nums):
        #     if nums[l] == 0 and nums[r]!=0:
        #         nums[l],nums[r] = nums[r],nums[l]
        #         l+=1
        #     elif nums[l]!=0:
        #         l+=1
        #     r+=1

        #Follow-up for minimizing the operations
        #Try to traverse array get the non-zero elements forward
        insert = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[insert] = nums[i]
                insert+=1
        
        for i in range(insert,len(nums)):
            nums[i] = 0 