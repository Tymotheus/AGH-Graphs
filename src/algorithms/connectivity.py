import copy

import src.objects.Graph as Graph

from src.algorithms.representation_conversions import convert_graph_representation
from src.algorithms.dfs import dfs, dfs_recursive


def is_graph_connected(g, show_vertices_flow=False):
    if isinstance(g, Graph.Graph):
        if g.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            if g.mode != "AM":
                convert_graph_representation(g, "AM")
            n = len(g.data)
            vertices_visits = [-1 for _ in range(n)]
            vertices_visits[0] = 1
            dfs_recursive(g, n, vertices_visits, v=0, component_number=1, show_vertices_flow=show_vertices_flow)
            for vertex_visited in vertices_visits:
                if vertex_visited == -1:
                    return False
            return True
    else:
        print("Passed argument is not a graph.")
        return False


def get_components_of_graph(g, show_components=False, show_vertices_flow=False):
    components = None
    if isinstance(g, Graph.Graph):
        if g.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            vertices_visits = dfs(g, show_vertices_flow)
            number_of_components = max(vertices_visits)
            components = [[] for _ in range(number_of_components)]
            for v in range(len(vertices_visits)):
                components[vertices_visits[v]-1].append(v)
            if show_components is True:
                for i in range(len(components)):
                    print(str(i + 1) + ")", end=''),
                    for j in range(len(components[i])):
                        print(" " + str(components[i][j] + 1), end='')
                    print()
    else:
        print("Passed argument is not a graph.")
    return components


def get_maximum_component_of_graph(g, show_maximum_component_result=False, show_components=False, show_vertices_flow=False):
    maximum_component = None
    if isinstance(g, Graph.Graph):
        if g.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            components = get_components_of_graph(g, show_components=show_components, show_vertices_flow=show_vertices_flow)
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
