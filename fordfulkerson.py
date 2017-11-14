#!/usr/bin/env python3


def ford_fulkerson(graph, source, sink):
    """Finds the maximum flow from source to sink in a directed graph.

    Args:
        graph: Node-arc list of the graph. Nodes are indexed from 0 to
            `len(graph) - 1`. The i-th index of the list contains
            the arcs adjacent to node i. The set of adjacent arcs is given as a
            dictionary. The keys <tuple> are the arcs and the value <float> is
            the capacity.

            Example (directed triangle graph):
            [
                {
                    (0, 1): 0.5,
                    (0, 2): 1.0,
                },
                {
                    (1, 2): 1.5,
                }
            ]
        source: Index of source node.
        sink: Index of sink node.

    Returns:
        A tuple of (value, flow).
        value <float>: Value of the maximum flow.

            Example (graph above, source=0, sink=2):
            value = 1.5

        flow <dict>: Flow on each arc. The keys for the dictionary are arcs
            represented as tuples. The value <float> is the flow on the arc.

            Example (graph above, source=0, sink=2):
            {
                (0, 1): 0.5,
                (0, 2): 1.0,
                (1, 2): 0.5,
            }
    """
    # TODO: implement me
    
    # remove / use for initialization
    value = 0.0
    flow = {}
    residual = {}
    aList=[]
    for node in graph:
        for arc in node:
            flow[arc] = 0.0
            
    for node in graph:
        for arc in node:
            residual[arc]=graph[arc[0]][arc]
            if (arc[1],arc[0]) in graph[arc[1]].keys():    
                residual[(arc[1],arc[0])]=graph[arc[1]][(arc[1],arc[0])]
            else:
                residual[(arc[1],arc[0])]=0
    label = []
    label=[0 for i in range(len(graph))]
    label[sink]=1
    while label[sink]==1:
        label=[ 0 for i in range(len(graph))]
        pred = [None for i in range(len(graph))]
        label[source]=1
        aList=[]
        aList.append(source)
        while len(aList) and label[sink]==0:
            i=aList[0]
            del aList[0]
            for arc in residual:
                if arc[0]==i and residual[(arc[0],arc[1])]:
                    if label[arc[1]]==0:
                        pred[arc[1]]=i
                        label[arc[1]]=1
                        aList.append(arc[1])
        if label[sink]==1:
            k=sink
            pathres=[]
            while k!=source:
                pathres.append(residual[(pred[k],k)])
                k=pred[k]
            delta=min(pathres)
            value+=delta
            k=sink
            while k!=source:
                residual[(pred[k],k)]-=delta
                residual[(k,pred[k])]+=delta
                k=pred[k]   
    for arc in flow:
        if graph[arc[0]][arc]>=residual[arc]:
            flow[arc]=graph[arc[0]][arc]-residual[arc]
    return (value, flow)

