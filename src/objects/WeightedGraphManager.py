import copy
import math

from random import randint

from src.objects.Graph import Graph
from src.objects.WeightedGraph import WeightedGraph
from src.algorithms.representation_conversions import convert_graph_representation
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

        if n == 1:
            return WeightedGraph()

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

        if n == 1:
            return WeightedGraph()

        g = construct_connected_graph_probability(n, p)
        return WeightedGraphManager.make_weighted_graph_from_simple_graph(g, w_min, w_max)

    @staticmethod
    def construct_complete_weighted_graph_from_grid_data(file_path=None):
        """
        Creates a complete weighted graph from metric data, that is:
            1. vertices in file are described in two columns representing vertices' X and Y positions on a grid
            2. each vertex should be described in one row
            3. weight of and edge between two vertices is Euclidean distance between them
        :param file_path: path to file with graph data. If not passed, the basic WeightedGraph object will be created.
        :return: WeightedGraph object of complete weighted graph represented by adjacency matrix
        """
        cwg = WeightedGraph()
        if file_path is None:
            print("No file was passed.")
        else:
            with open(file_path, 'r') as f:
                data = [[float(val) for val in line.split()] if line != '\n' else [] for line in f]
            n = len(data)
            cwg.data = [[None] * n for _ in range(n)]
            for i in range(1, n):
                for j in range(0, i):
                    cwg.data[i][j] = cwg.data[j][i] = math.sqrt(float(data[i][0] - data[j][0]) ** 2 + float(data[i][1] - data[j][1]) ** 2)
        return cwg
