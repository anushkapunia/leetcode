class Solution(object):
    def twoCitySchedCost(self, costs):
        sorted_costs = sorted(costs, key=lambda x: x[0] - x[1])  # Sorting the costs based on the difference between aCost and bCost
        n = len(costs) // 2  # Calculating n
        min_cost = 0

        for i in range(n):
            min_cost += sorted_costs[i][0]  # Adding the cost of flying to city A for the first n people
            min_cost += sorted_costs[i + n][1]  # Adding the cost of flying to city B for the remaining n people

        return min_cost
    
        