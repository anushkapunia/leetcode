class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -n
        
        r = 1
        while n>0:
            
            if n % 2 == 0:
                n = n//2
                x*=x
            else:
                n = n-1
                r = r*x
            
        return r   
            
        