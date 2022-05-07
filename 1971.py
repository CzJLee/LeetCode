# https://leetcode.com/problems/find-if-path-exists-in-graph/

class Graph:
    def __init__(self, n, edges):
        self.neighbors = {}
        for i in range(n):
            self.neighbors[i] = []
        
        for edge in edges:
            self.neighbors[edge[0]].append(edge[1])
            self.neighbors[edge[1]].append(edge[0])

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = Graph(n, edges)
        
        # DFS
        stack = []
        visited = set()
        
        stack.append(source)
        
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            
            if node in visited:
                continue
            else:
                visited.add(node)

                # Get neighbors
                neighbors = graph.neighbors[node]
                # Add to stack
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)
                    
        return False