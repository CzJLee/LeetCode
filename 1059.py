# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/solution/

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(i):
            seen.add(i)
            for j in graph[i]:
                if j == i or j in seen or not dfs(j):
                    return False
            seen.discard(i)
            return len(graph[i]) != 0 or i == destination
        
        graph = collections.defaultdict(set)
        seen = set()
        for a, b in edges:
            graph[a].add(b)
        return dfs(source)

        
        
        