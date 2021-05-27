import src.objects.Graph as Graph
import src.objects.Digraph as Digraph

from src.algorithms.representation_conversions import convert_graph_representation


def dfs(graph, show_vertices_flow=False):
    """Depth-First Search algorithm implementation. Returns the list of components to which vertices belong.
        graph - Graph or Digraph object
        show_vertices_flow - boolean whether to show the vertex flow during the DFS algorithm."""

    if isinstance(graph, Graph.Graph) or isinstance(graph, Digraph.Digraph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
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
        print("Passed argument is neither graph not digraph.")
    return None


def dfs_recursive(graph, n, v_component, v=0, component_number=1, show_vertices_flow=False):
    """Depth-First Search recursive function.
        graph - Graph or Digraph object
        n - number of vertices
        v_component - list of visited vertices:
            negative number means that vertex was now visited
            non-negative number represent the number of component to which the vertex belongs
        v - considered vertex (as a node of DFS)
        component_number - number of considered component
        show_vertices_flow - boolean whether to show the vertex flow during the DFS algorithm"""

    if isinstance(graph, Graph.Graph) or isinstance(graph, Digraph.Digraph):
        if graph.representation != "AM":
            convert_graph_representation(graph, "AM")
        for u in range(n):
            if graph.data[v][u]:
                if v_component[u] == -1:
                    if show_vertices_flow is True:
                        print(str(v+1) + " -> " + str(u+1))
                    v_component[u] = component_number
                    dfs_recursive(graph, n, v_component, u, component_number, show_vertices_flow)
    else:
        print("Passed argument is neither graph not digraph.")
    return None
