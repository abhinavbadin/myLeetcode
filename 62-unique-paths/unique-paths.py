class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. Recursive Solution 
        
        # def func(i,j):
        #     if i == 0 and j == 0:
        #         return 1 
        #     if i < 0 or j < 0:
        #         return 0
        #     up = func(i-1,j)
        #     left = func(i,j-1)
        #     return up + left
        
        # return func(m-1,n-1)

        #2. Memoization Solution 
        # def func(i,j,dp):
        #     if i == 0 and j == 0:
        #         return 1 
        #     if i < 0 or j < 0:
        #         return 0
        #     if dp[i][j]!= -1:
        #         return dp[i][j]
        #     up = func(i-1,j,dp)
        #     left = func(i,j-1,dp)
        #     dp[i][j] = up + left
        #     return dp[i][j]
        
        # dp = [[-1 for j in range(n)] for i in range(m)]
        # return func(m-1,n-1,dp)

        #3. Tabulation solution
        # dp = [[-1 for j in range(n)] for i in range(m)]

        # for i in range(0,m):
        #     for j in range(0,n):
        #         if i == 0 and j == 0:
        #             dp[i][j] = 1
        #             continue
        #         up, left = 0, 0
        #         if i > 0:
        #             up = dp[i-1][j]
        #         if j > 0:
        #             left = dp[i][j-1]
        #         dp[i][j] = up + left
        # return dp[m-1][n-1]

        #4. Space optimization
        prev = [0] * n

        for i in range(0,m):
            temp = [0] * n
            for j in range(0,n):
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue
                
                up, left = 0, 0
                if i > 0:
                    up = prev[j]
                if j > 0:
                    left = temp[j-1]
                
                temp[j] = up + left
            prev = temp
        return prev[n-1]

                    
  