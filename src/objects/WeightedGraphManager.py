import copy

from random import randint

from src.objects.Graph import Graph
from src.objects.WeightedGraph import WeightedGraph
from src.algorithms.representation_conversions import convert_graph_representation
from src.algorithms.connectivity import is_graph_connected
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
                w_max - maximum weight in weighted graph, by default equal to 10"""

        if not isinstance(graph, Graph):
            print("Passed argument is not a graph.")
            return
        if graph.representation != "AM":
            convert_graph_representation(graph, "AM")
        wg = WeightedGraph()
        wg.data = copy.deepcopy(graph.data)
        n = len(wg.data)
        for i in range(1, n):
            for j in range(0, i):
                if wg.data[i][j] is not None:
                    wg.data[i][j] = wg.data[j][i] = randint(w_min, w_max)
        return wg

    @staticmethod
    def construct_connected_weighted_graph_edge_number(n, m, w_min=1, w_max=10):
        """Creates and returns a connected weighted graph.
                n - number of vertices (should be greater than 0)
                m - number of edges (should be between n-1 and n*(n-1)/2)
                w_min - minimum weight in weighted graph, by default equal to 1
                w_min - maximum weight in weighted graph, by default equal to 10"""

        if n < 1:
            print("Random connected weighted graph cannot be created - number of vertices should be greater than 0.")
            return
        if m < n-1 or m > n*(n-1)/2:
            print("Random connected weighted graph cannot be created - number of edges should be between n-1 and n*(n-1)/2.")
            return

        g = construct_connected_graph_edge_number(n, m)
        return WeightedGraphManager.make_weighted_graph_from_simple_graph(g, w_min, w_max)

    @staticmethod
    def construct_connected_weighted_graph_probability(n, p, w_min=1, w_max=10):
        """Creates and returns a connected weighted graph of order n and probability of edge existence equal to p.
        It's weights are defined by passed arguments.
            n - number of vertices (should be greater than 0)
            p - probability with which each edge occurs independently (should be between 0 and 1)
            w_min - minimum weight in weighted graph, by default equal to 1
            w_min - maximum weight in weighted graph, by default equal to 10"""

        if n < 1:
            print("Random connected weighted graph cannot be created - number of vertices should be greater than 0.")
            return
        if p < 0.0 or p > 1.0:
            print("Random graph cannot be created - probability should be between 0 and 1.")
            return

        g = construct_connected_graph_probability(n, p)
        return WeightedGraphManager.make_weighted_graph_from_simple_graph(g, w_min, w_max)

    @staticmethod
    def read_from_file(path):
        """Creating weighted graph by reading adjacency matrix from file."""
        wg = WeightedGraph(path)
        if is_graph_connected(wg):
            return wg
        else:
            print("Graph read from file is not connected ")
