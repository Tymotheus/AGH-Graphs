import copy

from random import randint

from src.objects.Graph import Graph
from src.objects.WeightedGraph import WeightedGraph

from src.algorithms.connectivity import construct_connected_graph_edge_number, construct_connected_graph_probability


class WeightedGraphManager:
    """Representation of a simple weighted graph manager which allows to execute some operations connected with weighted graphs."""

    def __init__(self):
        """WeightedGraphManager constructor. Simply prints that an instance of the WeightedGraphManager have been created."""

        print("WeightedGraphManager has been created")

    @staticmethod
    def make_weighted_graph_from_simple_graph(graph, w_min=1, w_max=10):
        """Creates and return a weighted graph from a simple graph. It's weights are defined by passed arguments.
        graph - Graph object
        w_min - minimum weight in weighted graph, by default equal to 1
        w_min - maximum weight in weighted graph, by default equal to 10"""

        if not isinstance(graph, Graph):
            print("Passed argument is not a graph.")
            return
        wg = WeightedGraph()
        wg.data = copy.deepcopy(graph.data)
        n = len(wg.data)
        for i in range(1, n):
            for j in range(0, i):
                if wg.data[i][j]:
                    wg.data[i][j] = wg.data[j][i] = randint(w_min, w_max)
        return wg

    @staticmethod
    def construct_weighted_graph_edge_number(n, m, w_min=1, w_max=10):
        """Creates and return a weighted graph. It's weights are defined by passed arguments.
        n - number of graphs vertex (should be greater than 1),
        m - number of graphs edges (if m is smaller than n-1 is upgraded to n-1),
        w_min - minimum weight in weighted graph, by default equal to 1
        w_min - maximum weight in weighted graph, by default equal to 10"""

        if n < 2:
            n = 2
        if m < n-1:
            m = n - 1

        g = construct_connected_graph_edge_number(n, m)
        return WeightedGraphManager.make_weighted_graph_from_simple_graph(g, w_min, w_max)

    @staticmethod
    def construct_weighted_graph_probability(n, p, w_min=1, w_max=10):
        """Creates a connected graph of order n and probability of edge existence equal to p. 
        Such graph is constructed using construct_connected_tree() function, that is, using Prufer code.
        n - number of vertices (should be greater than 1)
        p - probability with which each edge occurs independently
        w_min - minimum weight in weighted graph, by default equal to 1
        w_min - maximum weight in weighted graph, by default equal to 10"""

        g = construct_connected_graph_probability(n, p)
        return WeightedGraphManager.make_weighted_graph_from_simple_graph(g, w_min, w_max)


    @staticmethod
    def read_from_file(path):
        """Creating weighted graph by reading adjacency matrix from file."""
        return WeightedGraph(path)
        # TO DO: reprezentacje? Czy tylko AM?

    @staticmethod
    def dijkstra(graph, origin):
        """"Method returns and prints matrix in which:
        matrix[0] is a list of distance from origin vertex to every other vertex
        matrix[1-...] are the dhotest paths from origin to every vertex
        vertex are counting from 1. 
        If input origin is greater than number of vertex then it is reduced to maximum vertex"""

        if origin < 1:
            origin = 1
            print("Origin has been upgraded to 1")

        if origin > len(graph.data):
            origin = len(graph.data)
            print("Origin has been reduced to " + str(origin))

        origin -= 1
        distance = {i: float('inf') for i in range(len(graph.data))}
        copyDistance = {i: float('inf') for i in range(len(graph.data))}

        distance[origin] = 0
        predecessor = [None for _ in range(len(graph.data))]

        S = []
        while len(S) < len(graph.data):
            (u, d) = min(copyDistance.items(), key=lambda x: x[1]) 
            S.append(u)
            copyDistance.pop(u)
            
            for v in range(len(distance)):
                if graph.data[v][u] and distance[v] > (distance[u] + graph.data[v][u]):
                    distance[v] = distance[u] + graph.data[v][u]
                    copyDistance[v] = distance[u] + graph.data[v][u]
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

        print("Strat s = " + str(origin+1))
        for v in range(len(graph.data)):
            print("d("+ str(v+1) +") = " + str(matrix[0][v]) + " ==> " + str(matrix[v+1]))

        return matrix