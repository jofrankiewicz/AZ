import numpy as np
import os

def random_graphs(n_v, max_val):
    points = np.random.randint(0,max_val,size=(n_v,2))
    name = "graph_"+str(n_v)+"_"+str(max_val)
    np.savetxt(name+"_.txt", points, fmt="%d")
    print("Wygenerowano plik: ", name+"_.txt")
   