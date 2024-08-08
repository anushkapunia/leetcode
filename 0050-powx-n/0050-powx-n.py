class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -n

        if n==0:
            return 1
        if n==1:
            return x
        
        h = self.myPow(x,n//2)
        
        if n%2 == 0:
            return h *h
        else:
            return h*h*x
        
        
  
        
        