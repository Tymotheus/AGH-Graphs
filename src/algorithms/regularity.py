from src.objects.Sequence import Sequence
import src.objects.Graph as Graph

from src.algorithms.degree_sequences import construct_graph_from_degree_sequence, is_degree_sequence
from src.algorithms.representation_conversions import convert_graph_representation


def is_graph_regular(graph):
    if isinstance(graph, Graph.Graph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            if graph.representation != "AM":
                convert_graph_representation(graph, "AM")
            k = sum(graph.data[0])
            for i in range(1, len(graph.data)):
                if sum(graph.data[i]) != k:
                    return False
            return True
    else:
        print("Passed argument is not a graph.")
        return False


def construct_k_regular_graph(n, k):
    g = Graph.Graph()
    if k < n:
        k_regular_degree_list = [k for _ in range(n)]
        seq = Sequence(k_regular_degree_list)
        if is_degree_sequence(seq):
            g = construct_graph_from_degree_sequence(seq)
        else:
            print("Sequence " + str(seq) + " is not a degree sequence of a graph.")
    else:
        print("k (regularity) should be less than n (number of vertices).")
    return g
