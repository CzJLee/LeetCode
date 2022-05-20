# https://leetcode.com/problems/unique-paths-ii/

import functools

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Use Dynamic Programming 
        # The number of ways to reach (h, w) is equal to the number of ways to get to it's two prior tiles
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        
        if obstacleGrid[height-1][width-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        visit_count = [[0] * width for _ in range(height)]
        visit_count[0][0] = 1
        
        @functools.cache
        def visit(h, w):
            if h < 0 or w < 0 or obstacleGrid[h][w] == 1:
                return 0
            elif h == 0 and w == 0:
                return 1
            return visit(h, w-1) + visit(h-1, w)
        
        return visit(height-1, width-1)