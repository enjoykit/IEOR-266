


#!/usr/bin/env python3


def max_weight_dijkstra(graph, source):
    """Determines the paths with minimum maximum weight from s to all nodes in a directed graph
    
    Args:
        graph: Node-arc list of the graph. Nodes are indexed from 0 to 'len(graph)-1'.
        source: Index of source code
   
    Returns:
        A tuple of (maxweight, predecessor).
        maxweight: List of maximum weights on the minimum max weight path from the source 
            to all nodes. The maximum weight is  'float('inf')' if the nodes is unreachable.
        predecessor: List of predecessors on the minimum max weight path from all nodes.
            Returns None for the source or when a node is unreachable.
    """
    maxweight = [float('inf') for i in range(len(graph))]
    predecessor = [None for i in range(len(graph))]
#keyvalue used to decide new node
    key = [float('inf')  for  i  in range(len(graph))]
#indicator == 1 when a node is alreday added
    ind = [0 for i in range(len(graph))]
    i = source
    ind[i] = 1
    maxweight[i] = -float('inf')
    for k in range(len(graph[i])):
        j = graph[i][k][0]
        key[j] = graph[i][k][1]
        maxweight[j] = key[j]
        predecessor[j] = i
    i = key.index(min(key))
    while key[i] < float('inf'):
#when all keyvalues are inf, no more reachable nodes
        ind[i] = 1
        key[i] = float('inf')
        for k in range(len(graph[i])):
            j = graph[i][k][0]
            c = graph[i][k][1]
            if (c < key[j] and ind[j] == 0):
                key[j] = c
                maxweight[j] = max(c,maxweight[i])
                predecessor[j] = i
        i = key.index(min(key))
    maxweight[source] = 0
    return (maxweight, predecessor)
    
    
