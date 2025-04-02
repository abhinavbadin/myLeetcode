class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n,d = dividend, divisor

        if n == d:
            return 1

        if n ==  -2147483648 and d == -1:
            return 2147483647
        
        if n ==  -2147483648 and d == 1:
            return -2147483648
        
        sign = False

        if n < 0 and d > 0:
            sign = True
        if n > 0 and d < 0:
            sign = True

        n = abs(n)
        d = abs(d)
        ans = 0
        
        while (n>=d):
            cnt = 0
            while (n>= (d<<cnt+1)):
                cnt+=1
            ans += 1<<cnt
            n -= d<<cnt

        if ans==(1<< 31) and sign:
            return float('inf')
        if ans==(1<< 31) and not sign:
            return float('-inf')  
        
        return ans if not sign else (-1 * ans)       