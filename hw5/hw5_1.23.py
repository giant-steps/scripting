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
def random_graph(nnodes):
    DG = nx.DiGraph()

    nodes = range(nnodes)

    DG.add_nodes_from(nodes)

    links = []

    random.seed(15)

    for i in nodes:     ## modify to remove double connections?
        for j in nodes:
            roll = random.randint(0, 4)

            if (roll == 0):
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

    nodenum = start

    covered = []
    covered.append(nodenum)


    """
    def new_adjacent(site, check):
        adjacent = [x for x in nx.all_neighbors(graph, site) if x not in check]
        check.extend(adjacent)
        return adjacent

    tier1 = new_adjacent(nodenum, covered)

    def next_tier(previous):    ## this function will take a list of nodes as input
        level = []
        for node in previous:   ## the list of nodes
            level.extend(new_adjacent(node, covered))
        return level

    objects = tier1
    """

    def new_adjacent(site, check):
        adjacent = [x for x in nx.all_neighbors(graph, site) if x not in check]
        return adjacent

    objects = new_adjacent(nodenum, covered)
    #print(objects) #####

    def next_tier(arg): ## this should take a list as input and return the neighbors of the first element not in covered

        #print(arg)

        count = 0
        output = ''

        #print(arg[count])      ##########


        while output == '':
            if arg[count] not in covered:
                output = arg[count]
            else:
                count += 1

        newlist = new_adjacent(output, covered)

        return newlist




    """
    while loop is: 
    neighbors of start node
    take first node that has not been searched (not in covered):
    get neighbors
    first neighbor not in covered
    and so on 
    
    iterate down til neighbors not including covered is empty list
    then go back to top, start again
    this is the while loop
    
    """

    go = True
    while go == True:



        if objects == []:
            go = False

        objects = next_tier(objects)

    return covered





def breadth_search(graph, start):
    nodenum = start

    covered = []
    covered.append(nodenum)

    def new_adjacent(site, check):
        adjacent = [x for x in nx.all_neighbors(graph, site) if x not in check]
        check.extend(adjacent)
        return adjacent

    tier1 = new_adjacent(nodenum, covered)

    def next_tier(previous):    ## this function will take a list of nodes as input
        level = []
        for node in previous:   ## the list of nodes
            level.extend(new_adjacent(node, covered))
        return level

    objects = tier1

    go = True
    while go == True:

        objects = next_tier(objects)

        if objects == []:
            go = False

    return covered


## main function definition
def main():
    graph = random_graph(10)
    #plt.show()     ## ***********

    print(depth_search(graph, 0))


## run main function
if __name__ == "__main__":
    main()