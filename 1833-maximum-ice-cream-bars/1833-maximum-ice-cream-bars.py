class Solution(object):
    def maxIceCream(self, costs, coins):
        c = sorted(costs)
        num = 0
        for i in c:
            if coins!=0 and coins >=i:
                coins-=i
                num +=1
        return num        
                