class Solution(object):
    def isIsomorphic(self, s, t):
        d = {}
        c = {}
        for a , b in zip(s,t):
            if (a in d and b != d[a]) or b in c and a != c[b]:
                return False
            else:
                d[a] = b
                c[b] = a
                
        return True