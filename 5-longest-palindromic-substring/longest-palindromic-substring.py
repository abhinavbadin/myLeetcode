class Solution:
    def longestPalindrome(self, s: str) -> str:
        residx = 0
        resLen = 0

        #Center Expansion(from center we move left and right directions) with 2-pointers
        for i in range(len(s)):
            #odd length
            l,r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > resLen:
                    residx = l
                    resLen = length
                l-=1
                r+=1

            #even length
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > resLen:
                    residx = l
                    resLen = length
                l-=1
                r+=1

        return s[residx: residx + resLen]  
