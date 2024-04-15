class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse= True)
        
         
        sum = 0
        for k in range(len(cost)):
            if (k+1)%3 == 0:
                pass
            else:
                sum+=cost[k]
         
        return sum