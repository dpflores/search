
def dijkstra(nodes, edges, source_index = 0):
    """
    param list nodes: the set of nodes
    param dict edges: the set of edges, e.g., {(node,node):distance}
    param int source_index: the index of the source node
    """
    
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source_index] = 0

    adjacent_nodes = {v: {} for v in nodes} # list of nodes
    for (u, v), w_uv in edges.items():
        adjacent_nodes[u][v] = w_uv         
        adjacent_nodes[v][u] = w_uv         # Creating a list of adjacent nodes and the path length for each node
    
    temporary_nodes = [v for v in nodes]    # Creating the temporary nodes, or nodes not explored
    while len(temporary_nodes)>0:
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}    # checking the values of updated path lengths for each node
        u = min(upper_bounds, key=upper_bounds.get)                     # Getting to the node with lower path length

        temporary_nodes.remove(u)           # removing the node from the unexplored or temporary nodes

        for v, w_uv in adjacent_nodes[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + w_uv)  # updating the distances of the nodes with the lower distance

    return path_lengths


    



nodes = [0, 1, 2, 3, 4, 5]
edges = {(0,1):1.0, (0,2):1.5, (0,3):2.0, (1,3):0.5, (1,4):2.5, (2,3):1.5, (3,5): 1.0, (4,5):2.0}

print(dijkstra(nodes, edges))
