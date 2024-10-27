class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        a = list(t)
        for i in range(len(s)):
            if s[i] in a:
                a.remove(s[i])
            else:
                return False
            
        return True
        