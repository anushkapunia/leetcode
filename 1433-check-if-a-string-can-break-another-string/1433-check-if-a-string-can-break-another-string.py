class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        a = min(s1,s2)
        b = max(s1,s2)
        for i in range(len(b)):
            if a[i]<=b[i]:
                continue
            else:
                return False
                break
        else:
            return True
    
        