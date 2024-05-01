class Solution(object):
    def maxProfit(self, prices):
        p = 0
        for i in range(len(prices)-1):
            if (prices[i+1]>prices[i]):
                d = prices[i+1]-prices[i]
                p+=d
                
        return p        
                
        
        