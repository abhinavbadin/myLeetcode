class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        
        prev1, prev = 1,1

        for i in range(2,n+1):
            curr = prev + prev1
            prev1 = prev
            prev = curr
        
        return prev