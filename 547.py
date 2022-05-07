class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class DisjointSet():
            def __init__(self, isConnected):
                self.root = [i for i in range(len(isConnected))]
                self.rank = [1 for _ in range(len(isConnected))]
                
                
                for i, row in enumerate(isConnected):
                    for j, connected in enumerate(row):
                        if connected:
                            self.join(i, j)
                
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
                return find_root(x) == find_root(y)
    
        # Create set
        cities = DisjointSet(isConnected)
        
        # Unique Roots
        roots = set()
        for i in range(len(isConnected)):
            roots.add(cities.find_root(i))
            
            
        return len(roots)
            
                
                    
                
            
        