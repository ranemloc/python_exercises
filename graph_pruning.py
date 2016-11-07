import sys

"""
This module implements a pruning algorithm (prune) on directed graphs.
The graph is given as a list of links between the nodes, each node being
a tuple of two elements: node of origin and target node.

The resulting graph begins empty.
The function "expand" loops over the original graph and when a link that is
connected to the visited nodes is found, it is moved from the original to the
resulting graph, thus expanding it.

The expansion runs in two different directions. First from the start node
to the subsequent (out) in the natural way of the directed graph, and afterwards
from the start node to the preceding nodes (in).
"""

def expand (src_graph, start_node, direction):
    out_graph = []
    visited = set()
    visited.add(start_node)
    if direction == 'out': # Search for subsequent links / nodes
        node_from = 0
        node_to = 1
    elif direction == 'in': # Search for preceding links / nodes
        node_from = 1
        node_to = 0

    keep_in_loop = True
    while keep_in_loop:
        keep_in_loop = False
        for link in src_graph:
            if link[node_from] in visited:
                out_graph.append(link)
                src_graph.remove(link)
                visited.add(link[node_to])
                keep_in_loop = True

    return src_graph, out_graph

def prune(start_graph, start_node):
    src_graph = list(start_graph)
    tmp_graph, out_graph = expand(src_graph, start_node, 'out')
    tmp_graph, in_graph = expand(tmp_graph, start_node, 'in')
    return out_graph + in_graph

def main():
    my_graph = [
        (1,4),
        (4,7),
        (7,2),
        (2,4),
        (2,0),
        (4,0),
        (3,5),
        (6,5),
        (5,0),
        (6,0),
        (4,4),
    ]
    start_node = int(sys.argv[1])
    print(prune(my_graph, start_node))

if __name__ == "__main__":
    main()
