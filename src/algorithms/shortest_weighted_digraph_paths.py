from math import dist
from src.objects.WeightedDigraph import WeightedDigraph
from src.objects.WeightedGraph import WeightedGraph
from src.algorithms.shortest_weighted_paths import dijkstra
import copy

def bellman_ford(wdg, origin=0, weight=[]):
    """ 
    """
    n = len(wdg.data)
    d  = [float('inf') for _ in range(n)]
    d[origin] = 0

    for _ in range(n-1):
        for u in range(0, n):
            for v in range(0, n):
                if wdg.data[u][v]:
                    w = weight[u][v] if len(weight) else wdg.data[u][v]
                    if d[v] > d[u] + w:
                        d[v] = d[u] + w
    for u in range(0, n):
        for v in range(0, n):
            w = weight[u][v] if len(weight) else wdg.data[u][v]
            if wdg.data[u][v] and d[v] > d[u] + w:
                return None
    return d

def distance_matrix_from_bellman_ford(wdg, show=True):
    """
    """
    n = len(wdg.data)
    if not isinstance(wdg, WeightedDigraph):
        print("Passed argument is not a weighted digraph.")
        return 

    matrix = [[] for _ in range(n)]

    for origin in range(n):
        d = bellman_ford(wdg, origin)
        if not d:
            print("There is a cycle with a negative sum of weights in the graph")
            return False
        matrix[origin] = d

    if show:
        print("Vertex distance matrix by Bellma-Ford algorithm:")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
    
    return matrix



def johnson(wdg, show=True):
    """
    """
    n = len(wdg.data)
    if not isinstance(wdg, WeightedDigraph):
        print("Passed argument is not a weighted digraph.")
        return 

    g = copy.deepcopy(wdg) 
    for i in range(n):
        g.data[i].append(0)
    g.data.append([1 for _ in range(n+1)])
    g.data[n][n] = 0
    weights = copy.deepcopy(g.data)
    weights[n] = [0 for _ in range(n+1)]

    h = bellman_ford(g, n, weights)
    if not h:
        print("There is a cycle with a negative sum of weights in the graph")
        return None

    for u in range(n+1):
        for v in range(n+1):
            if g.data[u][v]:
                weights[u][v] = weights[u][v] + h[u] - h[v]

    for u in range(n):
        for v in range(n):
            wdg.data[u][v] = g.data[u][v]

    wg = WeightedGraph()
    wg.data = wdg.data
    
    D = [[0 for _ in range(n)] for _ in range(n)]
    distance = [dijkstra(wg, u+1, weights=weights)[0] for u in range(n)]
    distanceT = [[distance[j][i] for j in range(n)] for i in range(n)]

    for u in range(n):
        for v in range(n):
            D[u][v] = distanceT[u][v] -h[u] + h[v] 
    
    if show:
        print("Vertex distance matrix by Johnson's algorithm:")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in D]))
    
    return D