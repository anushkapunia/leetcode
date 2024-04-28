class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        num = 0
        for i in costs:
            if coins!=0 and coins >=i:
                coins-=i
                num +=1
        return num        
                