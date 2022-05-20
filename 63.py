class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Use DFS, and each time you visit a new square, increment its visit count
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        
        if obstacleGrid[height-1][width-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        visit_count = [[0] * width for _ in range(height)]
        
        stack = [(0, 0)]
        
        while stack:
            h, w = stack.pop()
            visit_count[h][w] += 1
            
            if h < height - 1 and obstacleGrid[h+1][w] == 0:
                # Can move down
                stack.append((h+1, w))
            if w < width - 1 and obstacleGrid[h][w+1] == 0:
                # Can move right
                stack.append((h, w+1))
        
        return visit_count[height-1][width-1]