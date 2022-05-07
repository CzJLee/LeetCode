# https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def get_dist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        def find_all_edges(points):
            edges = []
            for p1 in points:
                for p2 in points:
                    if p1 != p2:
                        edges.append([p1, p2])
            return edges
        
        root = {}
        for point in points:
            root[tuple(point)] = tuple(point)
        
        def union(p1, p2):
            root1 = find(p1)
            root2 = find(p2)
            
            if root1 != root2:
                root[tuple(root1)] = root2
            
            return root1 != root2
        
        def find(p):
            if tuple(p) == tuple(root[tuple(p)]):
                return tuple(p)
            else:
                root[tuple(p)] = find(root[tuple(p)])
                return root[tuple(p)]
        
        def kruskals(edges):
            edges = sorted(edges, key = lambda x: get_dist(*x))
            
            min_tree_edges = []
            
            target_num_edges = len(points) - 1
            
            for edge in edges:
                if len(min_tree_edges) >= target_num_edges:
                    break
                
                # Check if adding the edge would form a loop
                # Form a loop if the two nodes to connect already share the same root
                if find(edge[0]) != find(edge[1]):
                    if (union(edge[0], edge[1])):  
                        min_tree_edges.append(edge)
            
            return min_tree_edges
            
        min_tree_edges = kruskals(find_all_edges(points))
        total_dist = 0
        for edge in min_tree_edges:
            total_dist += get_dist(*edge)
    
        return total_dist
                