# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create better data structures
        from collections import defaultdict
        
        connections = defaultdict(list)
        for time in times:
            connections[time[0]].append(time[1])
        
        weights = {}
        for time in times:
            connection = (time[0], time[1])
            weights[connection] = time[2]
            
        time_to_visit = {}
        for i in range(1, n+1):
            time_to_visit[i] = float("inf")
        
        time_to_visit[k] = 0
        
        queue = [k]
        visited = set()
        unvisited = set(range(1, n+1))
        
        def get_neighbors(node):
            return connections[node]
        
        def get_next_node(unvisited):
            if len(unvisited) == 0:
                return None
            weights_of_unvisited = [(time_to_visit[node], node) for node in unvisited]
            weights_of_unvisited.sort()
            next_node = weights_of_unvisited[0][1]
            if weights_of_unvisited[0][0] == float("inf"):
                return None
            else:
                return next_node
            
        node = get_next_node(unvisited)
        unvisited.discard(node)
        while node:            
            neighbors = get_neighbors(node)
            
            for neighbor in neighbors:
                # Get weight to visit each neighbor
                neighbor_time = weights[(node, neighbor)] + time_to_visit[node]
                if neighbor_time < time_to_visit[neighbor]:
                    time_to_visit[neighbor] = neighbor_time
                
            node = get_next_node(unvisited)
            unvisited.discard(node)
                
        # Get longest path
        all_times = sorted(list(time_to_visit.values()))
        
        if all_times[-1] == float("inf"):
            return -1
        else:
            print(all_times)
            return all_times[-1]