from src.objects.WeightedGraph import WeightedGraph
from src.algorithms.connectivity import is_graph_connected


def dijkstra(wg, origin, show=False, weights=[]):
    """"Performs Dijkstra algorithm on a WeightedGraph with non-negative values.
            wg - WeightedGraph object
            origin - source vertex from which shortest paths to other vertices will be find
            show - boolean whether to show distances and paths
        Returns a matrix of distances and paths between vertices
            matrix[0] - list of distances from source vertex (origin) to other vertices
            matrix[1]~matrix[n-1] - paths from source vertex (origin) to other vertices"""

    w = weights if len(weights) else wg.data
    
    if not isinstance(wg, WeightedGraph):
        print("Passed argument is not a weighted graph.")
        return
    if not is_graph_connected(wg):
        print("Passed argument is not connected.")
        return
    n = len(wg.data)
    for i in range(n):
        for j in range(n):
            if w[i][j] < 0:
                print("Cannot perform Dijkstra algorithm - passed weighted graph contains an edge with negative weight.")
                return

    if origin < 1 or origin > n:
        print("Wrong vertex! Origin should be an integer between 1 and "+str(n))
        return

    origin -= 1
    distance = {i: float('inf') for i in range(n)}
    copy_distance = {i: float('inf') for i in range(n)}
    distance[origin] = 0
    copy_distance[origin] = 0

    predecessor = [None for _ in range(n)]
    S = []
    while len(S) < n:
        (u, d) = min(copy_distance.items(), key=lambda x: x[1])
        S.append(u)
        copy_distance.pop(u)
        for v in range(len(distance)):
            if wg.data[v][u] and distance[v] > (distance[u] + w[v][u]):
                distance[v] = distance[u] + w[v][u]
                copy_distance[v] = distance[u] + w[v][u]
                predecessor[v] = u+1  

    matrix = [[] for _ in range(len(distance)+1)]
    matrix[0] = [i for i in distance.values()]
    for v in range(len(distance)):
        path = []
        element = predecessor[v]
        path.append(v+1)
        while element:
            path.append(element)
            element = predecessor[element-1]
        path.reverse()
        matrix[v+1] = path
    matrix[origin+1] = [origin+1]
    if show:
        print("Start s = " + str(origin+1))
        for v in range(n):
            print("d(" + str(v+1) + ") = " + str(matrix[0][v]) + " ==> " + str(matrix[v+1]))
    for i in range(1, n+1):
        for j in range(len(matrix[i])):
            matrix[i][j] -= 1
    return matrix


def create_vertex_distance_matrix(wg, show=False):
    """Returns matrix with distances between any two vertices.
            wg - WeightedGraph object
            show - boolean whether to show the distance matrix"""

    if not isinstance(wg, WeightedGraph):
        print("Passed argument is not a weighted graph.")
        return
    if not is_graph_connected(wg):
        print("Passed argument is not connected.")
        return
    n = len(wg.data)
    for i in range(n):
        for j in range(n):
            if wg.data[i][j] < 0:
                print("Cannot perform Dijkstra algorithm - passed weighted graph contains an edge with negative weight.")
                return

    distance_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        matrix = dijkstra(wg, i+1)
        distance_matrix[i] = matrix[0]
    if show:
        print("Vertex distance matrix:")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in distance_matrix]))
    
    return distance_matrix


def center_of_weighted_graph(wg, distance_matrix=[]):
    """Returns the center of a WeightedGraph, that is, a set of vertices whose sum of distances to other vertices is minimal.
            wg - WeightedGraph object
            distance_matrix - matrix with distances between any two vertices"""

    if not isinstance(wg, WeightedGraph):
        print("Passed argument is not a weighted graph.")
        return
    if not is_graph_connected(wg):
        print("Passed argument is not connected.")
        return

    n = len(wg.data)
    if not len(distance_matrix):
        distance_matrix = create_vertex_distance_matrix(wg)
    sums = {i: sum(distance_matrix[i]) for i in range(n)}
    min_sum = min(sums.values())
    indexes = [k+1 for k, v in sums.items() if v == min_sum]
    return [min_sum, *indexes]


def minimax_center_of_weighted_graph(wg, distance_matrix=[]):
    """ Finds the minimax center of a WeightedGraph, that is, a vertex whose distance to the farthest vertex is minimal.
            wg - WeightedGraph object
            distance_matrix - matrix with distances between any two vertices
        Returns a dictionary object with data connected with minimax center of a WeightedGraph
            minimax_center - list of index of minimax center vertex number
            sum_of_distance - sum of distances from minimax center to other vertices
            dist_to_farthest - distance from minimax center to it's farthest vertex"""

    if not isinstance(wg, WeightedGraph):
        print("Passed argument is not a weighted graph.")
        return
    if not is_graph_connected(wg):
        print("Passed argument is not connected.")
        return

    n = len(wg.data)
    if not len(distance_matrix):
        distance_matrix = create_vertex_distance_matrix(wg)
    maximums = {i: max(distance_matrix[i]) for i in range(n)}
    minimum = min(maximums.values())
    indexes = [k+1 for k, v in maximums.items() if v == minimum]
    return {"minimax_center": [i for i in indexes], "sum_of_distance": sum(distance_matrix[indexes[0]]), "dist_to_farthest": minimum}
