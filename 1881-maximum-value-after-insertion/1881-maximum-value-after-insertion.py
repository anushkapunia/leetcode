class Solution(object):
    def maxValue(self, n, x):
        isNegative, x, L, i = n[0] == '-', str(x), len(n), 0
        
        while i < L:
            if not isNegative and x > n[i]: break
            elif isNegative and x < n[i]: break
            i += 1
 
        return n[:i] + x + n[i:]
        