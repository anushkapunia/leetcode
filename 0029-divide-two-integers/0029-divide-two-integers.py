class Solution(object):
    def divide(self, dividend, divisor):
      
        # Handle division by zero
        if divisor == 0:
            return 2**31 - 1  # Return MAX_INT for division by zero
        
        # Get absolute values
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
        if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0):
            result = -result
        
        # Handle overflow
        return min(2**31 - 1, max(-2**31, result))
        