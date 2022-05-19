def get_valid_neighbors(matrix, node):
    height = len(matrix)
    width = len(matrix[0])
    
    h, w = node
    
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    neighbors = []
    
    for dh, dw in directions:
        if (h + dh) >= 0 and (h + dh) < height and (w + dw) >= 0 and (w + dw) < width:
            neighbors.append([h + dh, w + dw])
            
    return neighbors

from collections import defaultdict
def node_mappings(matrix):
    height = len(matrix)
    width = len(matrix[0])

    mappings_from = defaultdict(list)

    for h in range(height):
        for w in range(width):
            neighbors = get_valid_neighbors(matrix, [h, w])
            for nh, nw in neighbors:
                if matrix[nh][nw] > matrix[h][w]:
                    mappings_from[(h, w)].append((nh, nw))

    return mappings_from

import itertools
def get_entry_points(matrix, mappings_from):
    height = len(matrix)
    width = len(matrix[0])

    # Set of all possible coordinates
    all_nodes = set(itertools.product(range(height), range(width)))

    # Set of all coordinates that have an in node
    out_nodes = set()
    for list_of_out_nodes in mappings_from.values():
        out_nodes.update(list_of_out_nodes)
    
    # Entry points is set difference
    entry_points = all_nodes.difference(out_nodes)
    return entry_points

import numpy as np
import time
class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        # We can convert the data type into a Directed Acyclic Graph
        # The problem then becomes one of finding the longest path within a DAG
        # The graph is not necessarily fully connected
        # We know that we have to start at a node with no in nodes and end at a node with no out nodes
        
        # 1) Find all nodes with no in nodes as starting points
        # 2) For each possible start, create a grid that contains the maximum travel distance
        #    Start with every value = 0
        #    Add start to queue
        #    Remove front of queue
        #    Add neighbors to a queue
        #    Update distances of neighbors
        #    If distance of neighbor was updated, add it back to the queue
        # 3) Repeat until queue is empty 
        # 4) Largest value in the graph is largest number of edges, so total length is + 1
        
        mappings_from = node_mappings(matrix)

        entry_points = get_entry_points(matrix, mappings_from)

        max_distance = 0

        # Add all entry points to queue
        queue = list(entry_points)

        # Array of distances
        dist = np.zeros(shape=np.shape(matrix), dtype=int)

        while queue:
            # Get node
            node = queue.pop()

            # Update neighbors
            neighbors = mappings_from[node]
            for neighbor in neighbors:
                # If a greater distance is found
                if dist[node] + 1 > dist[neighbor]:
                    # Update neighbor
                    dist[neighbor] = dist[node] + 1
                    # Add it back to the queue
                    queue.append(neighbor)

        # Get max distance
        max_distance = np.amax(dist)
        
        return max_distance + 1