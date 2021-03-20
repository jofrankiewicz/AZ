import numpy as np
from utils import convert

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb: return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
    
    def find(self, a):
        if self.parent[a] == a:
            return a
        
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    

def kruskal(graph,n):
    mst = []
    nowa_macierz = convert(graph)
    new_graph = {
        'ver': [str(el) for el in range(n)],
        'edg': np.array(nowa_macierz)
    }
  
    sorted_array = new_graph['edg'][np.argsort(new_graph['edg'][:, 0])]

    ds = DisjointSet(n)
    for cost, u, v in list(list(sorted_array)):
        if ds.find(int(u)) != ds.find(int(v)):
            ds.union(int(u), int(v))
            mst.append((int(u),int(v),cost))
    return mst   