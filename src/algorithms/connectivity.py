import copy

from random import randint, sample, random

import src.objects.Graph as Graph
import src.objects.WeightedGraph as WeightedGraph

from src.algorithms.representation_conversions import convert_graph_representation
from src.algorithms.dfs import dfs, dfs_recursive


def is_graph_connected(graph, show_vertices_flow=False):
    """Returns True whether passed graph is connected and False otherwise.
        graph - Graph or WeightedGraph object
        show_vertices_flow - boolean whether to show the vertex flow during the DFS algorithm."""

    if not isinstance(graph, Graph.Graph) and not isinstance(graph, WeightedGraph.WeightedGraph):
        print("Passed argument is not a graph.")
        return False
    if graph.data is None:
        print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        return False
    else:
        if graph.representation != "AM":
            convert_graph_representation(graph, "AM")
        n = len(graph.data)
        v_component = [-1 for _ in range(n)]
        v_component[0] = 1
        dfs_recursive(graph, n, v_component, v=0, component_number=1, show_vertices_flow=show_vertices_flow)
        for vertex_visited in v_component:
            if vertex_visited == -1:
                return False
        return True


def construct_connected_tree(n):
    """Returns a connected tree of order n (graph without cycles). Such graph is constructed using Prufer code.
        n - number of vertices"""

    vertices = list(range(0, n))
    prufer_code = [randint(0, n-1) for _ in range(n-2)]

    g = Graph.Graph()
    g.representation = "AM"
    g.data = [[0] * n for _ in range(n)]

    while len(prufer_code) > 0:
        for elem in vertices:
            if elem not in prufer_code:
                g.data[elem][prufer_code[0]] = g.data[prufer_code[0]][elem] = 1
                vertices.remove(elem)
                prufer_code.remove(prufer_code[0])
                break
    g.data[vertices[0]][vertices[1]] = g.data[vertices[1]][vertices[0]] = 1
    return g


def construct_connected_graph_edge_number(n, m):
    """Returns a connected graph of order n and size m. Such graph is constructed using construct_connected_tree() function, that is, using Prufer code.
        n - number of vertices (should be greater than 0)
        m - number of edges (should be between n-1 and n*(n-1)/2)"""

    if n < 1:
        print("Graph cannot be created - number of vertices should be greater than 0.")
        return
    m_max = n * (n-1) / 2
    m_min = n-1
    if m < m_min or m > m_max:
        print("Graph cannot be created - number of edges should be between n-1 and n*(n-1)/2.")
        return
    g = construct_connected_tree(n)
    m -= m_min
    num_of_edges_to_choose = m_max - m_min

    indexes_of_existing_edges = sample(range(0, int(num_of_edges_to_choose)), m)
    index = 0
    for i in range(1, n):
        for j in range(0, i):
            if g.data[i][j] == 0:
                if index in indexes_of_existing_edges:
                    g.data[i][j] = g.data[j][i] = 1
                index = index + 1

    return g


def construct_connected_graph_probability(n, p):
    """Creates a connected graph of order n and probability of edge existence equal to p. Such graph is constructed using construct_connected_tree() function, that is, using Prufer code.
        n - number of vertices (should be greater than 0)
        p - probability with which each edge occurs independently (should be between 0 and 1)"""

    if n < 1:
        print("Graph cannot be created - number of vertices should be greater than 0.")
        return
    if p < 0 or p > 1:
        print("Graph cannot be created - probability should be between 0 and 1.")
        return

    g = construct_connected_tree(n)

    for i in range(1, n):
        for j in range(0, i):
            if g.data[i][j] == 0:
                if random() <= p:
                    g.data[i][j] = g.data[j][i] = 1

    return g


def get_components_of_graph(graph, show_components=False, show_vertices_flow=False):
    """Returns the list of vertices of a graph divided into connected components.
        graph - Graph object
        show_components - boolean whether to show found components
        show_vertices_flow - boolean whether to show the vertex flow during the DFS algorithm."""

    components = None
    if isinstance(graph, Graph.Graph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            v_component = dfs(graph, show_vertices_flow)
            number_of_components = max(v_component)
            components = [[] for _ in range(number_of_components)]
            for vertex in range(len(v_component)):
                components[v_component[vertex] - 1].append(vertex)
            if show_components is True:
                for i in range(len(components)):
                    print(str(i + 1) + ")", end=''),
                    for j in range(len(components[i])):
                        print(" " + str(components[i][j] + 1), end='')
                    print()
    else:
        print("Passed argument is not a graph.")
    return components


def get_largest_component_of_graph(graph, show_maximum_component_result=False, show_components=True, show_vertices_flow=False):
    """Returns the largest component of a graph.
        graph - Graph object
        show_maximum_component_result - boolean whether to show the largest component
        show_components - boolean whether to show found components
        show_vertices_flow - boolean whether to show the vertex flow during the DFS algorithm."""

    largest_component = None
    if isinstance(graph, Graph.Graph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            components = get_components_of_graph(graph, show_components=show_components,
                                                 show_vertices_flow=show_vertices_flow)
            maximum_number_of_vertices = len(components[0])
            largest_component_index = 0
            for i in range(len(components)):
                if len(components[i]) > maximum_number_of_vertices:
                    maximum_number_of_vertices = len(components[i])
                    largest_component_index = i
            largest_component = copy.deepcopy(components[largest_component_index])
            if show_maximum_component_result is True:
                print("Maximum component of the graph is component number " + str(largest_component_index + 1) + " (" + str(
                    maximum_number_of_vertices) + " vertices).")
    else:
        print("Passed argument is not a graph.")
    return largest_component
