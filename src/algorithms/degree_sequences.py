from src.objects.Sequence import Sequence
import src.objects.Graph as Graph

from src.algorithms.representation_conversions import convert_graph_representation


def isDegreeSequence(seq, show_steps=False):
    if isinstance(seq, Sequence):
        s = seq.data.copy()
        while True:
            s.sort(reverse=True)
            if show_steps:
                print(s)
            for elem in s:
                if elem != 0:
                    break
            else:
                return True
            if s[-1] == -1 or s[0] >= len(s):
                return False
            for i in range(1, s[0]+1):
                s[i] = s[i]-1
            del s[0]
    else:
        print("Passed argument is not a sequence.")


def get_degree_sequence_from_graph(g):
    if isinstance(g, Graph.Graph):
        s = Sequence()

        starting_representation = g.mode
        if starting_representation != "AL":
            convert_graph_representation(g, "AL")

        degree_seq_of_graph = [len(elem) for elem in g.data]
        s.read_sequence_from_list(degree_seq_of_graph)

        if starting_representation != "AL":
            convert_graph_representation(g, starting_representation)

        return s
    else:
        print("Passed argument is not a graph.")
