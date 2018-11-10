"""
This program will answer part one of hw5 for scripting
1) A function to create a random graph. This function will take a single parameter for the number
of nodes in the graph, and will return a NetworkX undirected graph object.
2) A function that implements a depth-first search of a graph. This function will take two
parameters: a NetworkX graph object and the node at which to start the search. It will return a
list of node names in the order they were visited. (Hint: use a stack to implement this algorithm)
3) A function that implements a breadth-first search of a graph. This function will take two
parameters: a NetworkX graph object and the node at which to start the search. It will return a
list of node names in the order they were visited. (Hint: use a queue to implement this
algorithm)

"""

## import statements
import sys

import networkx as nx
import matplotlib.pyplot as plt
import random

## function / class definitions
def random_graph(nnodes, connect):
    DG = nx.DiGraph()

    nodes = range(nnodes)

    DG.add_nodes_from(nodes)

    links = []

    random.seed(15)

    for i in nodes:
        for j in nodes:
            roll = random.randint(0, connect)

            if roll == 0:
                links.append((i, j))

    DG.add_edges_from(links)

    nx.draw_random(DG)  ## ************
    plt.draw()
    #plt.show()

    #return DG

    namenodes = {}

    for item in nodes:
        namenodes[item] = {'node number' : str(item)}

    #print(namenodes)

    nx.set_node_attributes(DG, namenodes)
    nodenames = nx.get_node_attributes(DG, 'node number')
    print(nodenames)



def depth_search(graph, start):
    pass

def breadth_search(graph, start):
    pass

## main function definition
def main():
    random_graph(10, 4)
    plt.show()

## run main function
if __name__ == "__main__":
    main()
