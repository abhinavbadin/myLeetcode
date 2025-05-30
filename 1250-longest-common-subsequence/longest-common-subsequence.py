class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # def func(ind1, ind2, t1, t2, dp):
        #     if ind1 < 0 or ind2 < 0:
        #         return 0
            
        #     if dp[ind1][ind2] != -1:
        #         return dp[ind1][ind2]
            
        #     if t1[ind1] == t2[ind2]:
        #         dp[ind1][ind2] =  1 + func(ind1 - 1, ind2 - 1, t1, t2, dp)
        #     else:
        #         dp[ind1][ind2] = max(func(ind1 - 1 , ind2, t1, t2, dp), func(ind1, ind2 - 1, t1, t2, dp))
            
        #     return dp[ind1][ind2]

        n = len(text1)
        m = len(text2)

        #dp = [[-1 for j in range(m+1)] for i in range(n+1)]

        prev = [0] * (m+1)
        # for i in range(n+1):
        #     dp[i][0] = 0
        
        for j in range(m+1):
            prev[j] = 0
        
        for i in range(1,n+1):
            curr = [0] * (m+1)
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
        return prev[j]
        # return func(n-1,m-1,text1, text2, dp)                