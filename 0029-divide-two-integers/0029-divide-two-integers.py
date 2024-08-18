class Solution(object):
    def divide(self, dividend, divisor):
    
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        end = abs(dividend)
        d = abs(divisor)
        
        r = 0
        while end >= d:
            s = 0
            while end >= (d << s):
                s += 1
            r += 1 << (s-1)
            end -= d << (s-1)
        
        if (dividend < 0) != (divisor < 0):
            r = -r
        
        return max(-2**31, min(2**31 - 1, r))