"""

Christopher Klocke


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
    DG = nx.Graph()     ## creates a NetworkX undirected graph object

    nodes = range(nnodes)
    DG.add_nodes_from(nodes)    ##  adds # of nodes requested by function argument

    links = []
    random.seed(20)
    for i in nodes:
        for j in nodes:
            roll = random.randint(0, 4) ## gives each combination of nodes a 1 in 4 chance of sharing an edge
            if (roll == 0):             ## (actually higher than 1 in 4 -- both directions)
                links.append((i, j))

    DG.add_edges_from(links)    ## add edges to connect nodes

    nx.draw_random(DG)  ## draw graph
    plt.draw()

    namenodes = {}

    for item in nodes:
        namenodes[item] = {'node number' : str(item)}

    nx.set_node_attributes(DG, namenodes)   ## set node names

    return DG   ## returns a NetworkX undirected graph object

def depth_search(graph, start):

    nodenum = start ## starts at node requested by function argument
    covered = []    ## will hold searched nodes in order
    covered.append(nodenum) ## add first node to searched nodes

    def new_adjacent(site, check):  ## takes node as input and returns list of adjacent nodes that have not yet been searched
        adjacent = [x for x in nx.all_neighbors(graph, site) if x not in check]
        return adjacent

    objects = new_adjacent(nodenum, covered)    ## sets 'objects' to neighbors of first node

    def next_tier(arg): ## takes a list of nodes as input and returns the neighbors of the first element not yet searched
        count = 0
        output = ''

        while count < len(arg):

            if arg[count] not in covered:
                output = arg[count]
                break

            else:
                count += 1

        if output == '':
            return ''

        else:
            covered.append(output)
            return new_adjacent(output, covered)

    go = True
    while go == True:
        objects = next_tier(objects)

        if objects == '':
            go = False

    return covered  ## returns searched nodes, in order

def breadth_search(graph, start):
    nodenum = start     ## starts at node requested by function argument

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
    plt.show()

    print(depth_search(graph, 0))
    print(breadth_search(graph, 0))


## run main function
if __name__ == "__main__":
    main()