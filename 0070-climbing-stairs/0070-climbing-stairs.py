class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return 1
        a, b = 1 , 2
        for i in range(3,n+1):
            c = a + b
            a = b
            b = c
        
        return b
        
            
        