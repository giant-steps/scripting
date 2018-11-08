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
    #print(nodenames)       ## ***********

    return DG


"""
what is the approach here...
    start with node zero 
    if there is an adjacent node, go to it (if multiple, pick one)
        repeat until there isn't a next node
    then go back to last node -- if another, pursue it; if not, go back another node
    
    repeat this process until all nodes have been searched
"""
def depth_search(graph, start):

    """
    nodecount = nx.number_of_nodes(graph)

    nx.get_node_attributes(graph, 'node number')

    for node in nx.nodes(graph):
        adjacent = nx.all_neighbors(graph, node)
        for neighbor in adjacent:
            print(neighbor)
    """


    """
    COMMENTING THIS SECTION and copying to work on, revert back to if needed
    start = [node for node in nx.nodes(graph) if node == 0]
    #print(start)

    stepone = nx.all_neighbors(graph, 0)
    tier1 = [x for x in stepone]
    #print(tier1[0])
    steptwo = nx.all_neighbors(graph, tier1[0])
    tier2 = [x for x in steptwo]
    print(tier2)

        ## for neighbors of tier1[0]: if not the one we came from, put in list -- then exhaust that list
    """




    #start = [node for node in nx.nodes(graph) if node == 0]
    # print(start)

    ## possible approach -- dictionary of dictionaries (or list of lists)?



    tier = 0

    pick = 0

    all = {}

    all[tier] = [x for x in nx.all_neighbors(graph, tier)]

    ## throw this in a while loop ^ & iterate thru tiers and nodes in each tier

    ## this structure should work for 2 and 3 -- just will move thru it in a different order





    #stepone = nx.all_neighbors(graph, tier)

    tier1 = [x for x in all[0]]
    # print(tier1[0])
    steptwo = nx.all_neighbors(graph, tier1[0])
    tier2 = [x for x in steptwo]
    print(tier2)

    ## for neighbors of tier1[0]: if not the one we came from, put in list -- then exhaust that list













    #for i in nx.nodes(graph):
        #print(i)


def breadth_search(graph, start):
    pass

## main function definition
def main():
    graph = random_graph(10, 4)
    #plt.show()     ## ***********

    depth_search(graph, 0)


## run main function
if __name__ == "__main__":
    main()