import random


def contraction(vertices, edges):
    graph_subsets = dict()
    while len(vertices) > 2:
        edge_index = random.randrange(len(edges))

        [u,v] = edges.pop(edge_index)

        if not(u in vertices) and not(v in vertices):
            add_at_parent(v,u, graph_subsets)
        elif not(u in vertices):
            vertices.remove(v)
            add_at_parent(v,u, graph_subsets)
        else:
            vertices.remove(u)
            add_at_parent(u,v, graph_subsets)

        i = 0
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

    return cut_edges


def is_loop(edge, graph_subsets):
    if edge[0] in graph_subsets and edge[1] in graph_subsets:
        return graph_subsets.get(edge[0]) == graph_subsets.get(edge[1]);
    return False

# add a node to a dictionary of subsets of a graph at its parent's root node
def add_at_parent(node,parent,graph_subsets):
    if not(parent in graph_subsets):
        graph_subsets.update({parent: parent})
        graph_subsets.update({node: parent})

    elif (parent in graph_subsets and node in graph_subsets):
        while parent != graph_subsets.get(parent):
            parent = graph_subsets.get(parent)
        while node != graph_subsets.get(node):
            node = graph_subsets.get(node)
        graph_subsets.pop(parent)
        graph_subsets.update({parent: node})
    else:
        while parent != graph_subsets.get(parent):
            parent = graph_subsets.get(parent)

        graph_subsets.update({node: parent})





vertices = []
edges = []
graph = [[1, 2, 3, 4],
        [2, 1, 3, 4],
        [3, 1, 2, 4],
        [4, 1, 2, 3, 5],
        [5, 4, 6, 7, 8],
        [6, 5, 7, 8],
        [7, 5, 6, 8],
        [8, 5, 6, 7]]

for row in range(len(graph)):
    node = graph[row][0]
    vertices.append(node)
    for col in range(1, len(graph[row])):
        incident_node = graph[row][col]
        edges.append([node, incident_node])




cop_vertices = vertices.copy()
cop_edges = edges.copy()


currentmin = contraction(cop_vertices, cop_edges)
for i in range(len(vertices)**2):
    print(i)
    cop_vertices = vertices.copy()
    cop_edges = edges.copy()
    curr = contraction(cop_vertices, cop_edges)
    if len(curr) < len(currentmin):
        currentmin = curr
print("end",currentmin)
