from random import random, sample, uniform

from src.objects.Digraph import Digraph

from src.algorithms.representation_conversions import convert_graph_representation


class DigraphManager:
    """Representation of a digraph manager which allows to execute some operations connected with digraphs."""

    def __init__(self):
        """DigraphManager constructor. Simply prints that an instance of the DigraphManager have been created."""

        print("DigraphManager has been created")

    @staticmethod
    def make_random_digraph_probability(n, p, show_info=True):
        """Creates a random digraph for given probability of arc existence (Gilbert model).
        n - number of vertices
        p - probability with which each arc occurs independently, must be between 0 and 1
        show_info - boolean whether to print information about the graph after its creation."""

        if n < 1:
            print("Random digraph cannot be created - number of vertices should be greater than 0.")
            return
        if p < 0 or p > 1:
            print("Random digraph cannot be created - probability should be between 0 and 1.")
            return

        dg = Digraph()
        dg.data = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if random() <= p:
                    dg.data[i][j] = 1
            dg.data[i][i] = None
        if show_info is True:
            print("Random digraph has been created (Gilbert model: n = " + str(n) + ", p = " + "{:.3f}".format(p) + ").")
            print("Digraph represented by adjacency matrix.")
        return dg

    @staticmethod
    def construct_transpose_digraph_from_digraph(digraph):
        """Creates and returns a transpose digraph of passed digraph.
                dg - Digraph object"""

        if not isinstance(digraph, Digraph):
            print("Passed argument is not a digraph.")
            return

        dg = Digraph()
        n = len(digraph.data)
        dg.data = [[None] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dg.data[i][j] = digraph.data[j][i]

        return dg
