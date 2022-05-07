# input: [[1,2], [2,3], [1,3], [3,4]], 1, 4
# output: [1,3,4]

def find_shortest_path_nx(edges, start, end):
    # Use NetworkX for easy Graphs
    import networkx as nx

    # Construct NetworkX graph from edges
    G = nx.Graph(edges)

    # Get shortest path
    return nx.shortest_path(G, start, end)

def find_shortest_path(edges, start, end):
    def build_graph(edges):
        # Build a dict mapping all vertices to a list of their edges

        # Get all vertices
        vertices = set()
        for edge in edges:
            vertices.add(edge[0])
            vertices.add(edge[1])
        
        # Build nodes dict
        nodes = {}
        for vertex in vertices:
            nodes[vertex] = []
        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])

        return nodes

    # Build graph
    graph = build_graph(edges)

    # Run BFS using a queue
    visited = []
    queue = []
    # Add a first path
    queue.append([start])

    while queue:
        # Get next path in queue
        path = queue.pop(0)
        # Get the current node, which is the last node in the path
        current_node = path[-1]
        
        # If the current node is at the end, we have created the shortest path in this BFS
        if current_node == end:
            return path
        
        # Otherwise, if the node is not yet visited, create new paths
        if current_node not in visited:
            # Get all connected nodes
            connected_nodes = graph[current_node]
            for node in connected_nodes:
                # For each connected node, create a new path
                extended_path = path.copy() + [node]
                queue.append(extended_path)
            # Update visited list
            visited.append(current_node)
    
    # If no path is found, return None
    return None

if __name__ == "__main__":
    edges = [[1,2], [2,3], [1,3], [3,4]]
    start = 1
    end = 4
    print(find_shortest_path_nx(edges, start, end))
    print(find_shortest_path(edges, start, end))
    print()

    edges = [[5, 4], [2, 5], [3, 6], [5, 7], [1, 4], [2, 4], [1, 3]]
    start = 1
    end = 7
    print(find_shortest_path_nx(edges, start, end))
    print(find_shortest_path(edges, start, end))
