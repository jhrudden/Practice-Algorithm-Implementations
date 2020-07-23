import random
import numpy

# finds the cross edges between 2 subsections of a MinCut of a given array
def find_contraction_cut_edges(vertices, edges):
    # edit of Kargers Randomized Contraction algorithm
    # instead of returning number of cross edges, return the actual edges

    # used to keep track of merged subsets of graph, without having to actually
    # merge nodes and shift edge values
    graph_subsets = dict()

    # when the number of subsets of the graph is two, then the graph has been
    # partitioned and return the results of the Min Cut
    while len(vertices) > 2:

        # graph edge at random
        edge_index = random.randrange(len(edges))
        [u,v] = edges.pop(edge_index)

        # merge v component to the u component and make sure all edges that
        # point to v actually point to u
        vertices.remove(v)
        add_at_parent(v,u, graph_subsets)

        i = 0

        # remove self loops ie. [u,v] where u == v
        while i < len(edges):
            curr_edge = edges[i]
            if is_loop(curr_edge, graph_subsets):
                edges.pop(i)
            i+=1

    cut_edges = []
    for edge in edges:
        if not(is_loop(edge, graph_subsets)):
            [u,v] = edge
            if not([u,v] in cut_edges or [v,u] in cut_edges):
                cut_edges.append(edge)

    # return the edges crossing the min cut
    return cut_edges

# does this edge refer to a loop in a graph
def is_loop(edge, graph_subsets):
    # when the merged subset of the graph a source of an edge is a part of
    # is equal to the subset that the incident node is apart of, then a cycle
    # has occured
    if edge[0] in graph_subsets and edge[1] in graph_subsets:
        return graph_subsets.get(edge[0]) == graph_subsets.get(edge[1]);

    # else no cycle occured
    return False

# add a node to a dictionary of subsets of a graph at its parent's root node
def add_at_parent(node,parent,graph_subsets):
    # if the source node isn't a part of a merged subset of a graph, make it a
    # head of a merged subset, then add the given node to the merged subset
    if not(parent in graph_subsets):
        graph_subsets.update({parent: parent})
        graph_subsets.update({node: parent})

    # if a parent and a given node are both apart a merged subsets, then merge
    # the subsets
    elif (parent in graph_subsets and node in graph_subsets):
        while parent != graph_subsets.get(parent):
            parent = graph_subsets.get(parent)
        while node != graph_subsets.get(node):
            node = graph_subsets.get(node)
        graph_subsets.pop(parent)
        graph_subsets.update({parent: node})

    # otherwise, just add a given node to the given parents merged subset
    else:
        while parent != graph_subsets.get(parent):
            parent = graph_subsets.get(parent)

        graph_subsets.update({node: parent})
