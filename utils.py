import math
import numpy as np
import collections
import random

def distance(x,y):
    return math.sqrt(((x[0]-y[0])**2)+((x[1]-y[1])**2))

def convert(dist):
    arr = list()
    for x in range(0,len(dist[0]-1)):
        for y in range(x+1,len(dist[0]-1)):
            x_val = x
            y_val = y
            value = dist[x][y]
            element = (value,x_val, y_val)
            arr.append(element)

    return arr

def find_odd_vertexes(mst):
    graph = {}                      # Creates a dictionary which contains going in and out information.
    for edge in mst:                # Run time V-1.
        #Initializing the values.
        if edge[0] not in graph:
            graph[edge[0]] = 0
        if edge[1] not in graph:
            graph[edge[1]] = 0
        #Adds the count of edge going or out to the respective city.
        graph[edge[0]] += 1
        graph[edge[1]] += 1
    #Odd vertexes.
    v = []
    for i in graph:
        if graph[i] % 2 == 1: #If odd then save it.
            v.append(i)
    return v

def minimum_weight_matching(mst, graph, odd_vertex):
    random.shuffle(odd_vertex)

    while odd_vertex:
        v = odd_vertex.pop()
        mini = np.inf
        u = -1
        closest = 0
        for u in odd_vertex:
            if(int(v)!=int(u)) and graph[u,v] < mini:
                mini = graph[u,v]
                closest = u
        mst.append((v,closest,mini))
        odd_vertex.remove(closest)


def find_eulerian_tour(mst, graph):
    near = {} # Edges next to the current city.
    for edge in mst: # Run time V-1.
        if edge[0] not in near:
            near[edge[0]] = []
        if edge[1] not in near:
            near[edge[1]] = []
        # Create a dictionary that will store the information of the cities near by, this is saving mst like in the first MST function.
        near[edge[0]].append(edge[1])
        near[edge[1]].append(edge[0])
    # finds the hamiltonian circuit
    start = mst[0][0] # The start of the tour.
    EP = [near[start][0]] # The tour.
    while len(mst) > 0:     # Runs for V-1 times.
        for i, v in enumerate(EP):  # Runs for 1+2+..+V
            if len(near[v]) > 0:
                break
        while len(near[v]) > 0:     # Runes for 2V+(2V-2)+..+0 
            w = near[v][0]          # Find the next city to choose.
            remove_edge(mst, v, w)  # Remove the city chosen.
            del near[v][(near[v].index(w))]
            del near[w][(near[w].index(v))]
            i += 1
            EP.insert(i, w) # Add it to the final answer.
            v = w
    return EP

def remove_edge(MatchedMST, v1, v2): # Use it to remove an edge from the tree once you reach it in the circuit traversal.
    for i, item in enumerate(MatchedMST):           
        if (item[0] == v2 and item[1] == v1) or (item[0] == v1 and item[1] == v2):
            del MatchedMST[i]
    return MatchedMST

def euclidean_metric(filename): #A funtion to initialise in case of euclidean metric.
    file = open(filename, "r")
    content = [ [int(chr) for chr in line.strip("\n").split(" ") if chr != ""] 
                for line in file.readlines()]
    n = len(content)
    dist = np.zeros((n,n)) #Initialize the dist
    #Populate the dist
    for i in range(n):
        for j in range(n):
            if(i==j):
                dist[i,j] = np.inf #Because we never want to get to the same place again (from any place)
            else:
                dist[i,j] = distance(content[i],content[j]) #Calculating the euclidean distance between all nodes from all nodes.
    #intializing the perm as the simplest traverse order 0..n perm
    perm = list(range(0,n))
    return(dist,perm,n)