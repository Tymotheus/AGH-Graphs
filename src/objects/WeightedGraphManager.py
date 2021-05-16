import copy

from random import randint

from src.objects.Graph import Graph
from src.objects.WeightedGraph import WeightedGraph
from src.algorithms.connectivity import is_graph_connected, get_largest_component_of_graph
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
        wGraph = WeightedGraph(path)
        if is_graph_connected(wGraph):
            return wGraph
        else:
            print("Graph read from file is not connected ")