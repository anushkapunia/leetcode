class Solution(object):
    def isPalindrome(self, s):
        l = 0 
        r = len(s)-1
        s1 = s.lower()
        while l<r:
            while l<r and not s1[l].isalnum():
                l+=1
            while l<r and not s1[r].isalnum():
                r-=1
            if s1[l] != s1[r]:
                return False
            l+=1
            r-=1
        return True
        