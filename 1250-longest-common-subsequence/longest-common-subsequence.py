class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def compare(i1,i2,dp):
            if i1 < 0 or i2 < 0:
                return 0
            
            if dp[i1][i2] != -1:
                return dp[i1][i2]
            
            if text1[i1] == text2[i2]:
                return 1 + compare(i1-1,i2-1,dp)
            
            dp[i1][i2] =  0 + max(compare(i1-1,i2,dp), compare(i1,i2-1,dp))
            return dp[i1][i2]
        
        m = len(text1)
        n = len(text2)
        #dp = [[0 for j in range(n+1)] for i in range(m+1)]

        prev = [0]*(n+1)

        for i in range(1,m+1):
            curr = [0]*(n+1)
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
        
        return prev[n]
        #return compare(m-1 , n-1, dp) 