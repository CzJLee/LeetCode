"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""

import collections
class Solution:
    def create_node_map(self, edges) -> dict[int, int]:
        node_map = collections.defaultdict(set)
        for x, y in edges:
            node_map[x].add(y)
            node_map[y].add(x)

        return node_map

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # Conjecture: There can only be up to two MHT
        # Assume node x is the root. 
        # You can shift to another node to balance uneven sides. 
        # You can't do this more than once. 
        # Another equal MHT can't be more than 1 shift away, since any other root would have x as a child branch.

        # Start with any node
        # Find the futhest node
        # Then set that node as root
        # Find the futher node
        # MHT is the middle of this connection
        if n == 1:
            return [0]

        node_map = self.create_node_map(edges)

        furthest_dist = 0
        furthest_node = None

        stack = []
        stack.append((0, 0))
        visited = set()

        while stack:
            node, dist = stack.pop()
            if node in visited:
                continue
            visited.add(node)

            if dist > furthest_dist:
                furthest_dist = dist
                furthest_node = node
            
            neighbors = node_map[node]
            for node in neighbors:
                if node not in visited:
                    stack.append((node, dist+1))
        
        start_dist = 0
        start_node = None

        stack = []
        stack.append((furthest_node, 0))
        visited = set()

        while stack:
            node, dist = stack.pop()
            if node in visited:
                continue
            visited.add(node)

            if dist > start_dist:
                start_dist = dist
                start_node = node
            
            neighbors = node_map[node]
            for node in neighbors:
                if node not in visited:
                    stack.append((node, dist+1))

        # Now connect start node to furtherst node

        stack = []
        stack.append((start_node, [start_node]))
        visited = set()

        while stack:
            node, path = stack.pop()
            if node in visited:
                continue
            visited.add(node)

            if node == furthest_node:
                break
            
            neighbors = node_map[node]
            for node in neighbors:
                if node not in visited:
                    updated_path = path + [node]
                    stack.append((node, updated_path))
        
        # Find middle of path
        mht_roots = []
        print(path)
        if len(path) % 2 == 0:
            # Is even
            # There are two nodes
            mht_roots.append(path[len(path) // 2])
            mht_roots.append(path[len(path) // 2 - 1])
        else:
            # Is odd
            # There is only one node
            mht_roots.append(path[len(path) // 2])

        return mht_roots

