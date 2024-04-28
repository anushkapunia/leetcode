class Solution(object):
        def maxIceCream(self, costs, coins):
            
            costs.sort()
            for i in range(len(costs)):
                coins -= costs[i]
                if coins < 0:
                    return i
            return len(costs)

        