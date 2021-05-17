from src.objects.WeightedGraph import WeightedGraph
from src.algorithms.connectivity import is_graph_connected


def kruskal(wg):
    """ Finds a minimum spanning tree of a connected weighted graph.
            wg - WeightedGraph object, should be connected
        Returns a dictionary object with data connected with minimum spanning tree.
            mst - found minimum spanning tree as weighted graph
            mst_edges - set of edges which creates the minimum spanning tree
            weight_sum - sum of weights of edges which create the minimum spanning tree"""

    if not isinstance(wg, WeightedGraph):
        print("Passed argument is not a weighted graph.")
        return
    if not is_graph_connected(wg):
        print("Passed argument is not connected.")
        return

    n = len(wg.data)
    mst = WeightedGraph()
    mst.data = [[0] * n for _ in range(n)]
    mst_edges = []
    weight_sum = 0
    components = [i for i in range(n)]
    num_of_components = n

    edges = []
    for i in range(0, n-1):
        for j in range(i+1, n):
            if wg.data[i][j]:
                edges.append([i, j, wg.data[i][j]])
    third_list_argument = lambda li: li[2]
    edges.sort(key=third_list_argument)

    while len(edges) and num_of_components != 1:
        edge = edges.pop(0)
        if components[edge[0]] != components[edge[1]]:
            mst.data[edge[0]][edge[1]] = mst.data[edge[1]][edge[0]] = edge[2]
            mst_edges.append([edge[0], edge[1]])
            weight_sum += edge[2]
            old_component = components[edge[1]]
            new_component = components[edge[0]]
            for i in range(n):
                if components[i] == old_component:
                    components[i] = new_component
            num_of_components -= 1

    return {"mst": mst, "mst_edges": mst_edges, "weight_sum": weight_sum}
