import random
import copy

# count the number of cross edges in a MinCut of a given graph
def count_split_edge_contraction(vertices, edges):
    # Kargers contraction appraoch to finding Min Cut

    # randomly choose an edge then merge the two nodes correct edges connected
    # to two nodes, then delete self loops
    # when there are only two nodes left, the graph has been partitioned
    # and a Min Cut has been found
    while len(vertices) > 2:

        # pick an edge
        edge_index = random.randrange(0,len(edges))
        [u,v] = edges.pop(edge_index)

        # merge u with v, then delete u from vertices list
        vertices.remove(u)

        next_round_edges = []

        # update nodes connected to u to point to v
        # and delete edges that are circular ie. Edge = [u,v] and u == v
        for i in range(len(edges)):
            if edges[i][0] == u:
                edges[i][0] = v;

            elif edges[i][1] == u:
                edges[i][1] = v;

            if edges[i][0] != edges[i][1]:
                next_round_edges.append(edges[i])
        edges = next_round_edges

    # Min Cut has been found, so count the return the amount of edges between
    # the partitioned sub graphs
    return len(edges)


# 41 - 61 prepares info for adj list of vertices, edges from a txt img for
# testing
data = open("adj_list.txt").read().splitlines()
graph = []
for line in data:
    row = []
    line = line.split()
    for element in line:
        row.append(int(element))
    graph.append(row)

vertices = []
edges = []
for row in range(len(graph)):
    node = graph[row][0]
    vertices.append(node)
    for col in range(1, len(graph[row])):
        incident_node = graph[row][col]
        edge = [node, incident_node]
        if not edge in edges and [edge[1],edge[0]] not in edges:
            edges.append(edge)



runs = []

# As Kargers algorithm relies on choosing random edges to merge/contract
# Min Cut produced may not be the min'est of Min Cuts, in order to improve
# the probability of finding the Min Cut instead of running the algorithm
# once, the algorithm runs |V|^2 times as the prob of finding min cut
# is >= (1/|V|^2)
for i in range(len(vertices)**2):
    print(len(vertices)**2- i)
    cop_vertices = copy.deepcopy(vertices)
    cop_edges = copy.deepcopy(edges)
    current = count_split_edge_contraction(cop_vertices, cop_edges)
    runs.append(current)
print(runs)
print("end",min(runs))
