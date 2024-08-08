class Solution(object):
    def myPow(self, x, n):
 
        if n == 0:
            return 1
        if x == 0:
            return 0
    
    
        if n < 0:
            x = 1 / x
            n = -n
            
        r = 1
        while n > 0:
            if n%2== 1:
                r*=x
                
            x*=x
            n = n // 2
            
        return r
                
            
      

  
      