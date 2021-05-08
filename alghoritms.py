import numpy as np
from utils import euclidean_metric, minimum_weight_matching, minimum_weight_matching, find_eulerian_tour, find_odd_vertexes
from prim import prim
from kruskal import kruskal

class Graph:
    def __init__(self,n,filename):
        (self.dist, 
        self.perm, 
        self.n) = euclidean_metric(filename) 

    def tourValue(self): #Cost of the tour value as described by specifications.
        return sum([self.dist[i,j] for i,j in 
                    zip(self.perm, self.perm[1:]+self.perm[0:1])])

    def twoApproximation(self):
        end = []
        def l(d, k):
            end.append(k)
            d[k].sort()
            for i in d[k]:
                if(i in d):
                    l(d, i)
                else:
                    end.append(i)
            return end
        mst = prim(self.dist.copy(),self.n)
        self.perm = l(mst,0)
        self.perm = [i for n, i in enumerate(self.perm) if i not in self.perm[:n]]


    def christofide(self):
        mst = kruskal(self.dist.copy(), self.n) # Create the minimum spanning tree.
        mst_cost = 0
        for i in mst:
            mst_cost+=i[2]
        odd_vertex = find_odd_vertexes(mst)          
        minimum_weight_matching(mst, self.dist.copy(), odd_vertex) 
        eulerian = find_eulerian_tour(mst.copy(), self.dist.copy()) #Find the eulerian tour.
        visited = set([]) #Find the hamiltonian cycle.
        self.perm = []
        for i in eulerian:
            if(not i in visited):
                visited.add(i)
                self.perm.append(i)
        return(mst_cost)
    