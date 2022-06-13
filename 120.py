# https://leetcode.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        depth = len(triangle)
        
        # Create min sum triangle
        min_sums = []
        
        # min sum for first level is equal to the first level
        level_sums = triangle[0]
        min_sums.append(level_sums)
        
        
        # DP appraoch 
        # Find min sum to arrive at every location 
        for i in range(1, depth):
            level_sums = []
            # Add first element
            level_sums.append(min_sums[i-1][0] + triangle[i][0])
            for j in range(1, len(triangle[i]) - 1):
                min_sum = min(min_sums[i-1][j], min_sums[i-1][j-1]) + triangle[i][j]
                level_sums.append(min_sum)
            # Add last element
            level_sums.append(min_sums[i-1][-1] + triangle[i][-1])
            min_sums.append(level_sums)
        
        # Get smallest sum on last layer
        return min(min_sums[-1])
    