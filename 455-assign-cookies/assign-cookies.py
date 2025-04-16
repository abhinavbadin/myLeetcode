class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        consume_cookies = 0
        g.sort()
        s.sort()
        l,r=0,0
        while l < len(g) and r < len(s):
            if g[l]<=s[r]:
                consume_cookies+=1
                l+=1
            r+=1
        return consume_cookies