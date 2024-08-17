class Solution(object):
    def divide(self, dividend, divisor):
     
        # Constants for 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle division by zero
        if divisor == 0:
            return INT_MAX
        
        # Handle overflow cases
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the quotient
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Convert to positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        
        # Apply the sign to the result
        return min(max(sign * quotient, INT_MIN), INT_MAX)
        