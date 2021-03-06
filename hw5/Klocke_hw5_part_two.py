"""
This program will answer part two of hw5 for scripting

4) Create and draw a random graph with 10 nodes (show the node labels on the drawing and save
the figure to a file).

5) Run a depth-first search on the random graph. Show the order in which the nodes were visited.

6) Run a breadth-first search on the random graph. Show the order in which the nodes were
visited.

7) Use either search algorithm to determine whether the random graph is connected (DON'T use the NetworkX is_connected()
function).

8) Also, do 5 through 7 above using the example karate club graph shown in class (start at node 0).

turn in:
1. A Python module containing the functions specified above (from part 1).
2. A word document showing the commands for importing and using the module, along with the
output for 4-8 above (please paste the figure of the random graph in this document).

"""

## import statements
import sys
import matplotlib.pyplot as plt
import networkx as nx
import Klocke_hw5_part_one_beta as search

## function / class definitions

## main function definition
def main():
    graph1 = search.random_graph(10)
    plt.show()

    print(search.depth_search(graph1, 0))
    print(search.breadth_search(graph1, 0))

    ## do length of list returned by search compared to input value of 10 -- if equal, graph is connected
        ## give a brief explanation of this

    KG = nx.karate_club_graph()
    nx.draw(KG, with_labels=True)

    plt.show()

    print(search.depth_search(KG, 0))
    print(search.breadth_search(KG, 0))

    ## add #7 for karate club

    ## run main function
if __name__ == "__main__":
    main()

