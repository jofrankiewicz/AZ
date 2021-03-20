import math
import numpy as np

def prim(graph, n):      # A function to create a minimum spanning tree from a graph.
    reached     = set([0])                  # Set of nodes already used.
    mst         = {}                            # Minimum Spanning tree initialized.
    graph[:,0] = np.inf
    for i in range(n-1): # Loops until all the nodes are added. (time looped = V) 
        toUse, toReach = 0,0 # Node used in order to reach node.
        mini = math.inf
        for row in reached:
            cm = np.min(graph[row])
            if(cm<mini):
                mini    = cm
                toUse   = row
                toReach = np.argmin(graph[row])
                    
        mst[toUse] = mst[toUse]+[toReach] if toUse in mst else [toReach]
        reached.add(toReach)
        graph[:,toReach] = np.inf
    return(mst)