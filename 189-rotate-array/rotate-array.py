class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #solution - 1 : Ofcourse using the extra memory 
        #solution - 2 : Using constant extra space

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start +=1
                end -=1
        
        n = len(nums)
        k = k % n #this is because if k value is greater than len of array 

        reverse(0,n-1) #reverse all 
        reverse(0,k-1) #reverse till k elements
        reverse(k,n-1) #reverse rest of them 

        