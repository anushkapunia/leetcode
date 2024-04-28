

class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()  # Sort costs in ascending order
        num = 0

        for cost in costs:
            index = bisect_right(costs, coins)
            if index > num:
                coins -= costs[num]
                num += 1
            else:
                break

        return num        