class Solution(object):
    def maximumUnits(self, b, t):
        b.sort(key = lambda x : x[1] , reverse = True)
        m = 0
        b_take = 0
        for bn , un in b:
            if t <= 0:
                break
            b_take = min(t , bn)
            m += b_take * un
            t -= b_take
            
        return m
            
            
            
        