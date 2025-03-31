class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = 1<<n
        arr=[]

        for num in range(0, subsets):
            li= []
            for i in range(0,n):
                if num & (1<<i):
                    li.append(nums[i])
            arr.append(li)
        
        return arr