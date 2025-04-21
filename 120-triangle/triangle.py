class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def func(i,j,n,arr,dp):
            if i == n-1:
                return arr[n-1][j]
            if dp[i][j] != -1:
                return dp[i][j]
            d = arr[i][j] + func(i+1,j,n,arr,dp)
            dg = arr[i][j] + func(i+1,j+1,n,arr,dp)
            dp[i][j] = min(d,dg)
            return dp[i][j]
        n = len(triangle)
        dp = [[-1 for i in range(n)] for j in range(n)]
        return func(0,0,n,triangle,dp)