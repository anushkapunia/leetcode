class Solution(object):
    def reverseString(self, s):
        n = len(s)
        temp,i = 0,0
        while i< n//2:
            s[i] , s[n-i-1] = s[n-i-1] , s[i] 
            i+=1
            
         
        