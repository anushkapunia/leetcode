class Solution(object):
    def findContentChildren(self, g, s):
        count = 0
        g.sort()
        s.sort()
        i,j = 0,0
        while i < len(g) and j < len (s):
            if s[j]>=g[i]:
                count+=1
                i+=1
            j+=1
        return count     
        