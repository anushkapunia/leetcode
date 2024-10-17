class Solution(object):
    def isPalindrome(self, x):
        a = x
        r = 0
        while x> 0:
            n = x %10
            x = x//10
            r = (r*10) + n 
            
        if a == r:
            return True
        else:
            return False
        