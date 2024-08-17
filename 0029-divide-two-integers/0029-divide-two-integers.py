class Solution(object):
    def divide(self, dividend, divisor):
  
        divid = abs(dividend)
        div = abs(divisor)
        
        result = 0
        
        while divid >= div:
            shift = 0
            while divid >= (div << shift):
                shift += 1
            
            result += (1 << (shift - 1))
            divid -= div << (shift - 1)
        
        # Handle negative cases
        if (dividend < 0) ^ (divisor < 0):
            result = -result
        
        # Handle overflow
        return max(-2**31, min(2**31-1 , result))