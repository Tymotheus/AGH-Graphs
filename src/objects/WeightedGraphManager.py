import copy

from random import randint

from src.objects.Graph import Graph
from src.objects.WeightedGraph import WeightedGraph


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
