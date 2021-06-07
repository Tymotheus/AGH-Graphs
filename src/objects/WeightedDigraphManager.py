import copy

from random import randint

from src.objects.Digraph import Digraph
from src.objects.WeightedDigraph import WeightedDigraph
from src.algorithms.representation_conversions import convert_graph_representation
from src.algorithms.strong_connectivity import construct_strongly_connected_digraph


class WeightedDigraphManager:
    """Representation of a weighted graph manager which allows to execute some operations connected with weighted digraphs."""

    def __init__(self):
        """WeightedDigraphManager constructor. Simply prints that an instance of the WeightedDigraphManager have been created."""

        print("WeightedDigraphManager has been created")

    @staticmethod
    def make_weighted_digraph_from_digraph(digraph, w_min=1, w_max=10):
        """Creates and returns a weighted digraph from a digraph. It's weights are defined by passed arguments.
                digraph - Digraph object
                w_min - minimum weight in weighted graph, by default equal to 1
                w_max - maximum weight in weighted graph, by default equal to 10"""

        if not isinstance(digraph, Digraph):
            print("Passed argument is not a digraph.")
            return
        if digraph.representation != "AM":
            convert_graph_representation(digraph, "AM")
        wdg = WeightedDigraph()
        wdg.data = copy.deepcopy(digraph.data)
        n = len(wdg.data)
        for i in range(n):
            for j in range(n):
                if i != j and wdg.data[i][j]:
                    wdg.data[i][j] = randint(w_min, w_max)
        return wdg

    @staticmethod
    def construct_strongly_connected_weighted_digraph_probability(n, p, w_min=1, w_max=10):
        """Creates and returns a strongly connected weighted digraph of order n and probability of arc existence equal to p.
        It's weights are defined by passed arguments.
            n - number of vertices (should be greater than 0)
            p - probability with which each arc occurs independently (should be between 0 and 1)
            w_min - minimum weight in weighted graph, by default equal to 1
            w_max - maximum weight in weighted graph, by default equal to 10"""

        if n < 1:
            print("Strongly connected weighted digraph cannot be created - number of vertices should be greater than 0.")
            return
        if p < 0.0 or p > 1.0:
            print("Strongly connected weighted digraph cannot be created - probability should be between 0 and 1.")
            return

        scwdg = construct_strongly_connected_digraph(n, p)
        return WeightedDigraphManager.make_weighted_digraph_from_digraph(scwdg, w_min, w_max)
