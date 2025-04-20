class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def func(i,j, grid,dp):
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            up = grid[i][j] + func(i-1,j,grid,dp)
            left = grid[i][j] + func(i,j-1,grid,dp)
            dp[i][j] = min(up,left)
            return dp[i][j]
        
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(n)] for j in range(m)]
        return func(m-1,n-1,grid,dp)