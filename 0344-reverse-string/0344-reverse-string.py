class Solution(object):
    def reverseString(self, s):
        n = len(s)
        temp,i = 0,0
        while i< n//2:
            temp =s[i]
            s[i] = s[n-i-1]
            s[n-i-1] = temp
            i+=1
            
        return s    
        