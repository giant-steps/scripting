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

    ## he says to use a stack
    ## so, list.append()
    ## list.pop()
    ## add to end/top, remove from end/top

    ## think about how to implement this



    nodenum = start

    covered = []
    covered.append(nodenum)




    def new_adjacent(site, check):
        adjacent = [x for x in nx.all_neighbors(graph, site) if x not in check]
        check.extend(adjacent)
        return adjacent



    tier1 = new_adjacent(nodenum, covered)
    print(tier1)   ########

    for node in tier1:
        #print(node)     ########
        newvar = new_adjacent(node, covered)



    print(covered)




def breadth_search(graph, start):
    nodenum = start

    covered = []
    covered.append(nodenum)

    def new_adjacent(site, check):
        adjacent = [x for x in nx.all_neighbors(graph, site) if x not in check]
        check.extend(adjacent)
        return adjacent

    tier1 = new_adjacent(nodenum, covered)

    for node in tier1:
        newvar = new_adjacent(node, covered)

    print(covered)


## main function definition
def main():
    graph = random_graph(10)
    #plt.show()     ## ***********

    breadth_search(graph, 0)


## run main function
if __name__ == "__main__":
    main()