class Solution(object):
    def carPooling(self, trips, capacity):
        change = [0]*1001
        
        for p , f ,t in trips:
            change[f]+=p
            change[t]-=p
        
        check = 0
        for c in change:
            check+=c
            if check > capacity:
                return False
            
        return True
            
            
        