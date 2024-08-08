class Solution(object):
    def myPow(self, x, n):
 
        if n == 0:
            return 1
        if x == 0:
            return 0
    
    # Handle negative exponents
        if n < 0:
            x = 1 / x
            n = -n
    
        result = 1
        while n > 0:
        # If n is odd, multiply result by x
            if n % 2 == 1:
                result *= x
        # Square x and halve n
            x *= x
            n //= 2
    
        return result
    
        