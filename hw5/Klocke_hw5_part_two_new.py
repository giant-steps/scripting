"""
Christopher Klocke
Assignment #5
Submitted: November 8th, 2018

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
import Klocke_hw5_part_one_new as search

## function / class definitions

## main function definition
def main():
    graph1 = search.random_graph(10)
    plt.show()

    depth_rand = search.depth_search(graph1, 0)
    print(depth_rand)
    breadth_rand = search.breadth_search(graph1, 0)
    print(breadth_rand)

    if nx.number_of_nodes(graph1) == len(depth_rand):
        print('This graph is connected.')

    KG = nx.karate_club_graph()
    nx.draw(KG, with_labels=True)

    plt.show()

    depth_karate = search.depth_search(KG, 0)
    print(depth_karate)
    breadth_karate = search.breadth_search(KG, 0)
    print(breadth_karate)

    if nx.number_of_nodes(KG) == len(depth_karate):
        print('This graph is connected.')

    ## run main function
if __name__ == "__main__":
    main()

