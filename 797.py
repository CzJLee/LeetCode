# https://leetcode.com/problems/all-paths-from-source-to-target/solution/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path_stack = []
        valid_paths = []
        
        end = len(graph) - 1
        
        path_stack.append([0])
        
        while path_stack:
            path = path_stack.pop()
            if path[-1] == end:
                valid_paths.append(path)
            
            # Get all future paths
            neighbors = graph[path[-1]]
            
            # print(f"{neighbors=}")
            
            for neighbor in neighbors:
                if neighbor not in path:
                    path_stack.append(path + [neighbor])
                    
        return valid_paths
                    
            
                
            
            