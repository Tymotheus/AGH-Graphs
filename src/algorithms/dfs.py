import src.objects.Graph as Graph

from src.algorithms.representation_conversions import convert_graph_representation


def dfs(graph, show_vertices_flow=False):
    if isinstance(graph, Graph.Graph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
            return None
        else:
            if graph.representation != "AM":
                convert_graph_representation(graph, "AM")
            n = len(graph.data)
            component_number = 0
            v_component = [-1 for _ in range(n)]
            for v in range(n):
                if v_component[v] == -1:
                    component_number += 1
                    v_component[v] = component_number
                    dfs_recursive(graph, n, v_component, v, component_number, show_vertices_flow)
            return v_component
    else:
        print("Passed argument is not a graph.")
        return None


def dfs_recursive(graph, n, v_component, v=0, component_number=1, show_vertices_flow=False):
    if graph.representation != "AM":
        convert_graph_representation(graph, "AM")
    for u in range(n):
        if graph.data[v][u] == 1:
            if v_component[u] == -1:
                if show_vertices_flow is True:
                    print(str(v+1) + " -> " + str(u+1))
                v_component[u] = component_number
                dfs_recursive(graph, n, v_component, u, component_number, show_vertices_flow)
