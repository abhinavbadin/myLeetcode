class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        prev = [0] * n

        for i in range(m):
            curr = [0] * n
            for j in range(n):
                
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                
                elif i == 0 and j == 0:
                    curr[j] = 1
                
                else:
                    up = prev[j] if i > 0 else 0
                    left = curr[j-1] if j > 0 else 0
                    curr[j] = up + left
            prev = curr
        
        return prev[n-1]