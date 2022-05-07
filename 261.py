# https://leetcode.com/problems/graph-valid-tree/submissions/

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        class DisjointSet():
            def __init__(self, edges, n):
                self.root = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]
                
                for edge in edges:
                    self.join(edge[0], edge[1])
                
            def find_root(self, x):
                if x == self.root[x]:
                    return x
                else:
                    self.root[x] = self.find_root(self.root[x])
                    return self.root[x]
                
            def join(self, x, y):
                x_root = self.find_root(x)
                y_root = self.find_root(y)
                
                if x_root != y_root:
                    if self.rank[x_root] > self.rank[y_root]:
                        # Use x as root
                        self.root[y_root] = x_root

                    elif self.rank[y_root] > self.rank[x_root]:
                        # Use y as root
                        self.root[x_root] = y_root

                    else:
                        # Both have equal rank
                        self.root[y_root] = x_root
                        self.rank[x_root] += 1
                        
            def is_connected(self, x, y):
                return self.find_root(x) == self.find_root(y)
                        
        # Create set
        tree = DisjointSet(edges, n)

        # Valid tree if fully connected and number of edges is exactly n-1
        
        # Check if fully connected
        for i in range(n):
            for j in range(i+1, n):
                if not tree.is_connected(i, j):
                    return False
        
        # Check number of edges
        num_edges = len(edges)
        
        return num_edges == n-1
        
class FastSolution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        root = list(range(n))
        def find(x):
            if root[x] == x:
                return x
            else:
                return find(root[x])
        def union(xy):
            x, y = map(find, xy)
            root[x] = y
            # Handle cycles
            return x != y
        return all(map(union, edges))

# [[0,1], [1,2], [2, 0], [3, 4]]
# 0 1
# 1 2
# 2 2
