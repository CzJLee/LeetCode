# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        
        # To make the union(a, b) function more useful, one can return a boolean value in the function to indicate whether the merging actually happens or not. For example, union(a, b) would return true when a and b (and their respective groups) are merged together, and false when a and b are already in the same group and thus do not need to be merged together.      
        return rootX != rootY

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        
        group = UnionFind(n)
        
        disjoint_groups = n
        
        for timestamp, a, b in logs:
            if group.union(a, b):
                disjoint_groups -= 1
                
            if disjoint_groups == 1:
                return timestamp
            
        return -1
        
        