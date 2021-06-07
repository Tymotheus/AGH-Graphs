import copy

from src.objects.Sequence import Sequence
import src.objects.Graph as Graph

from src.algorithms.representation_conversions import convert_graph_representation


def is_degree_sequence(sequence, show_steps=False):
    """ Implementation of Havel-Hakimi algorithm.
            sequence - Sequence object
            show_steps - boolean whether to show the steps of checking process
        Returns True whether passed sequences is a degree sequence and False otherwise."""

    if isinstance(sequence, Sequence):
        if len(sequence.data) > 0:
            seq_copy = copy.deepcopy(sequence.data)
            count_odd = 0
            for elem in seq_copy:
                if elem % 2 == 1:
                    count_odd += 1
            if count_odd % 2 == 1:
                return False
            while True:
                seq_copy.sort(reverse=True)
                if show_steps:
                    print(seq_copy)
                for elem in seq_copy:
                    if elem != 0:
                        break
                else:
                    return True
                if seq_copy[-1] == -1 or seq_copy[0] >= len(seq_copy):
                    return False
                for i in range(1, seq_copy[0] + 1):
                    seq_copy[i] += - 1
                del seq_copy[0]
        else:
            print("Passed argument is an empty sequence.")
    else:
        print("Passed argument is not a sequence.")
    return False


def get_degree_sequence_from_graph(graph):
    """Returns the degree sequence from a passed graph.
        graph - Graph object"""

    if isinstance(graph, Graph.Graph):
        seq = Sequence()
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            if graph.representation != "AM":
                convert_graph_representation(graph, "AM")

            degree_seq_of_graph = [sum(elem) for elem in graph.data]
            seq.read_sequence_from_list(degree_seq_of_graph)
        return seq
    else:
        print("Passed argument is not a graph.")
    return


def construct_graph_from_degree_sequence(sequence):
    """Returns a graph from passed sequence if it's a degree sequence.
            sequence - Sequence object, should be degree sequence"""

    graph = Graph.Graph()
    if isinstance(sequence, Sequence):
        if is_degree_sequence(sequence):
            n = len(sequence)

            graph.representation = "AM"
            graph.data = [[0] * n for _ in range(n)]
            v_and_d = [[i, sequence[i]] for i in range(n)]

            while True:
                v_and_d.sort(key=lambda li: li[1], reverse=True)
                if v_and_d[0][1] == 0:
                    break
                for j in range(1, v_and_d[0][1]+1):
                    v_and_d[j][1] -= 1
                    graph.data[v_and_d[0][0]][v_and_d[j][0]] = graph.data[v_and_d[j][0]][v_and_d[0][0]] = 1
                del v_and_d[0]
        else:
            print("Passed sequence is not a degree sequence of a graph.")
    else:
        print("Passed argument is not a sequence.")
    return graph
