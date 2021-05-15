import argparse
import time
import glob
import argparse
import numpy as np
from alghoritms import Graph
from generate_files import random_graphs

def main():
    print('Rozpoczęcie działania programu rozwiązującego problem TSP')

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-g', '--generation', dest='generation', type=bool, default=False,
                        help='generate graph data')
    parser.add_argument('-nv', '--n_val', dest='n_val', type=int, default=600,
                        help='number of vertices')
    parser.add_argument('-mv', '--max_val', dest='max_val', type=int, default=10000,
                        help='maximum value in graph data')
    
    args = vars(parser.parse_args())
    if args['generation']:
        random_graphs(args['n_val'], args['max_val'])

    mylist = [f for f in glob.glob("graph*")]

    for filename in mylist:
        g = Graph(-1, filename)

        name_details=filename.split('_')
        
        methods = [(g.twoApproximation,"2_Approximation"),
                (g.christofide, "Christofides")]
        f = open("results.txt", "a")
        for i, (method, name) in enumerate(methods):
            start = time.time()
            method()
            result = g.tourValue()
            end = time.time()
            result_time = end-start 
            print("Ilość wierzchołków: {}, Max waga: {}, Algorytm: {}, Wartość cyklu: {}, Czas: {}".format(name_details[1], name_details[2], name, result, result_time))

            f.write(str(name_details[1]))
            f.write(" ")
            f.write(str(name_details[2]))
            f.write(" ")
            f.write(name)
            f.write(" ")
            f.write(str(result))
            f.write(" ")
            f.write(str(result_time))
            f.write('\n')

        f.close()  

main()