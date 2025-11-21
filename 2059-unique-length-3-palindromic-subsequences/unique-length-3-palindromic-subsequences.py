class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #3 - len palindrome is X Y X -> so first and last occurance same. 
        #Its just putting unique chars in middle

        res = 0

        for c in range(26):
            #You loop through each charcter from 'a' to 'z'
            ch = chr(ord('a')+c)

            left = s.find(ch) #first occurance
            right = s.rfind(ch) #last occurance

            # We need at least 3 positions: x _ x
            if left!= -1 and right != -1 and right - left > 1:

                middle = s[left+1:right]

                #now get uniq chars in the middle array
                res+= len(set(middle))

        return res  