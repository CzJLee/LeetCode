# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS
        goal = (len(grid)-1 , len(grid)-1)
        
        start = (0, 0)
        if grid[start[0]][start[1]] != 0 or grid[goal[0]][goal[1]] != 0:
            return -1
        
        visited = [[0 for _ in range(goal[1] + 1)] for _ in range(goal[0] + 1)]
        
        queue = [[start]]
        
        def get_valid_neighbors(node):
            perm = [-1, 1, 0]
            
            possible_neighbors = []
            
            for x in perm:
                for y in perm:
                    possible_neighbors.append((node[0] + x, node[1] + y))
            possible_neighbors.pop()
            
            valid_neighbors = []
            
            for neighbor in possible_neighbors:
                if neighbor[0] <= goal[0] and neighbor[0] >= 0 and neighbor[1] <= goal[1] and neighbor[1] >= 0:
                    if grid[neighbor[0]][neighbor[1]] == 0:
                        valid_neighbors.append(neighbor)
                        
            return valid_neighbors
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            visited[node[0]][node[1]] = 1
            
            if node == goal:
                return len(path)
            
            # Get neighbors
            neighbors = get_valid_neighbors(node)
            
            for neighbor in neighbors:
                if visited[neighbor[0]][neighbor[1]] == 0:
                    queue.append(path + [neighbor])
                    
        return -1
                    
        
            