class Solution(object):
    def myPow(self, x, n):
  
        if n < 0:
            x = 1 / x
            n = -n
        
        # Base case
        if n == 0:
            return 1.0
        
        # Recursive case
        half = self.myPow(x, n // 2)
        
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
        