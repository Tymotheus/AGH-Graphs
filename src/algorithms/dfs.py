import src.objects.Graph as Graph

from src.algorithms.representation_conversions import convert_graph_representation


def dfs(g, show_vertices_flow=False):
    if isinstance(g, Graph.Graph):
        if g.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
            return None
        else:
            if g.mode != "AM":
                convert_graph_representation(g, "AM")
            n = len(g.data)
            component_number = 0
            vertices_visits = [-1 for _ in range(n)]
            for v in range(n):
                if vertices_visits[v] == -1:
                    component_number += 1
                    vertices_visits[v] = component_number
                    dfs_recursive(g, n, vertices_visits, v, component_number, show_vertices_flow)
            return vertices_visits
    else:
        print("Passed argument is not a graph.")
        return None


def dfs_recursive(g, n, vertices_visits, v=0, component_number=1, show_vertices_flow=False):
    if g.mode != "AM":
        convert_graph_representation(g, "AM")
    for u in range(n):
        if g.data[v][u] == 1:
            if vertices_visits[u] == -1:
                if show_vertices_flow is True:
                    print(str(v+1) + " -> " + str(u+1))
                vertices_visits[u] = component_number
                dfs_recursive(g, n, vertices_visits, u, component_number, show_vertices_flow)
