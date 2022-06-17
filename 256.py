# https://leetcode.com/problems/paint-house/
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Constraint: No two houses next to each other can be painted the same
        # Minimize: Cost
        # DP
        
        # Create a nx3 array, that indicates the cost of painting that house that color and all all previous houses
        # For n house, for each color, take the min of the two other colors before it. 
        
        if len(costs) == 1:
            return min(costs[0])
        
        # Make a copy
        total_costs = costs.copy()
        
        for i in range(1, len(costs)):
            r, g, b = costs[i]
            # Red
            total_costs[i][0] = r + min(total_costs[i-1][1], total_costs[i-1][2])
            # Green
            total_costs[i][1] = g + min(total_costs[i-1][0], total_costs[i-1][2])
            # Blue
            total_costs[i][2] = b + min(total_costs[i-1][0], total_costs[i-1][1])
        
        return min(total_costs[-1])