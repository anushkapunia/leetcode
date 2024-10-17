class Solution(object):
    def reverse(self, x):
        t = x
        x = abs(x)
        rev = 0
        while x> 0:
            n = x%10
            x = x//10
            rev = (rev*10)+n
            
        if t < 0 and  -2**31 <= rev <= 2**31-1:
            return -rev
        elif -2**31 <= rev <= 2**31-1:
            return rev
        
        return 0