import copy

import src.objects.Graph as Graph

from src.algorithms.representation_conversions import convert_graph_representation
from src.algorithms.dfs import dfs, dfs_recursive


def is_graph_connected(graph, show_vertices_flow=False):
    if isinstance(graph, Graph.Graph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
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
    else:
        print("Passed argument is not a graph.")
        return False


def get_components_of_graph(graph, show_components=False, show_vertices_flow=False):
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


def get_maximum_component_of_graph(graph, show_maximum_component_result=False, show_components=False, show_vertices_flow=False):
    maximum_component = None
    if isinstance(graph, Graph.Graph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            components = get_components_of_graph(graph, show_components=show_components,
                                                 show_vertices_flow=show_vertices_flow)
            maximum_number_of_vertices = len(components[0])
            maximum_component_index = 0
            for i in range(len(components)):
                if len(components[i]) > maximum_number_of_vertices:
                    maximum_number_of_vertices = len(components[i])
                    maximum_component_index = i
            maximum_component = copy.deepcopy(components[maximum_component_index])
            if show_maximum_component_result is True:
                print("Maximum component of the graph is component number " + str(maximum_component_index + 1) + " (" + str(
                    maximum_number_of_vertices) + " vertices).")
    else:
        print("Passed argument is not a graph.")
    return maximum_component
