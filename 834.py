"""
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

Example 1:


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
Example 2:


Input: n = 1, edges = []
Output: [0]
Example 3:


Input: n = 2, edges = [[1,0]]
Output: [1,1]
 

Constraints:

1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.
"""

import collections

class Solution:
    def build_tree(self, edges: list[list[int]]) -> dict[int, set[int]]:
        tree = collections.defaultdict(set)
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)
        
        return tree


    def bfs_memo(self, start, tree, dist_array):
        """BFS starting at start, over tree, adding to dist array."""

        queue = []
        queue.append((start, 0))
        seen = set()

        while queue:
            node, dist = queue.pop(0)
            seen.add(node)
            dist_array[start][node] = dist

            # Early stopping dynamic programming part
            # If we encounter a node we already have info for, we can fill out dist
            if node < start:
                for i in range(len(dist_array)):
                    dist_array[start][i] = min(dist_array[start][node] + dist_array[node][i], dist_array[start][i])
            else:
                # Only add new searches if we haven't seen this node yet.
                for neighbor in tree[node]:
                    if neighbor not in seen:
                        queue.append((neighbor, dist+1))



    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        """First use DFS to get distance from one node to all others. Then use properties of a tree to fill out an array that contains the distance from one node to any other node. Then fill out answer."""

        # Let dist[i][j] be the distance from node i to node j. 
        # Then dist[i][j] == dist[j][i]

        # Build dist array
        dist = [[float("inf")] * n for _ in range(n)]

        tree = self.build_tree(edges)

        for i in range(n):
            self.bfs_memo(i, tree, dist)

        answer = [sum(row) for row in dist]
        return answer