# https://leetcode.com/problems/rotting-oranges/

import numpy as np
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        grid = np.array(grid)
        m = grid.shape[0]
        n = grid.shape[1]
        
        
        def get_neighbors(node):
            adjacencies = [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1)
            ]
            
            possible_neighbors = [node + adj for adj in adjacencies]
            valid_neighbors = []
            for neighbor in possible_neighbors:
                if neighbor[0] >= 0 and neighbor[0] < m and neighbor[1] >= 0 and neighbor[1] < n:
                    if grid[neighbor[0], neighbor[1]]== 1:
                        valid_neighbors.append(neighbor)
            return valid_neighbors
        
        # Find starting rotten oranges
        
        rotten = np.transpose(np.where(grid == 2))
        if np.all(grid == 0):
            return 0
        
        queue = [orange for orange in rotten]
        
        time = 0
        
        while queue:
            rotten = queue
            queue = []
            for orange in rotten:
                neighbors = get_neighbors(orange)
                for neighbor in neighbors:
                    queue.append(neighbor)
                    grid[neighbor[0], neighbor[1]] = 2
            
            time += 1
            
        if len(np.transpose(np.where(grid == 1))) > 0:
            return -1
        else:
            return time-1
            