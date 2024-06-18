class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        total_gas, total_cost = 0, 0
        start = 0

        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]

        if total_gas < total_cost:
            return -1
 
        tank = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return start

        