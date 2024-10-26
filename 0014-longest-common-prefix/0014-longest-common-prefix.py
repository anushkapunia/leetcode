class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        n = len(strs)
        f = strs[0]
        l = strs[n-1]
        a = []
        for i in range(min(len(f), len(l))):
            if f[i] != l[i]:
                return ''.join(a)
            a.append(f[i])
            
        return ''.join(a)
            
        
        