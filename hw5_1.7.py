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

    for i in nodes:     ## modify to remove double connections?
        for j in nodes:
            roll = random.randint(0, connect)

            if roll == 0:
                links.append((i, j))

    DG.add_edges_from(links)

    nx.draw_random(DG)  ## ************
    plt.draw()
    #plt.show()

    namenodes = {}

    for item in nodes:
        namenodes[item] = {'node number' : str(item)}

    nx.set_node_attributes(DG, namenodes)
    #nodenames = nx.get_node_attributes(DG, 'node number')

    return DG



def depth_search(graph, start):

    all = {}    ## dictionary of new adjacent nodes from each node
                ## key is node number and value is list of adjacent (unvisited) node numbers

    tier = 0
    nodenum = start     ## start at node 0 -- this is fed in as function argument

    def all_append(dict, level, id, graph_id, check):
        dict[(level, id)] = [x for x in nx.all_neighbors(graph_id, id) if x not in check]
        ## dict is all, level is tier, id is nodenum, graph_id is graph, check is covered

    tierset = tier
    nodenumset = nodenum
    covered = []    ## nodes that have been searched
        ## using covered in this way will ignore connections to nodes that have already been searched

    all_append(all, tier, nodenum, graph, covered)


    covered.append(nodenum)

    tier += 1
    for adjacent in all[(tierset, nodenumset)]:
        nodenum = adjacent
        covered.append(nodenum)

        all_append(all, tier, nodenum, graph, covered)

    ## run this for loop again and again -- will need to put it into larger loop
    ## that should do it












    """
    possibly use recursion -- wrap this process of going one level deeper if there is another level into
    its own function, then run that function within a loop? 
    
    """

    ## throw this in a while loop ^ & iterate thru tiers and nodes in each tier

    ## this structure should work for 2 and 3 -- just will move thru it in a different order

    print(all)
    print(covered)  ## also need to show order in which nodes were visited -- this is 'covered'

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