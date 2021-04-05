import copy

from src.objects.Sequence import Sequence
import src.objects.Graph as Graph

from src.algorithms.representation_conversions import convert_graph_representation


def is_degree_sequence(seq, show_steps=False):
    if isinstance(seq, Sequence):
        if len(seq.data) > 0:
            s = copy.deepcopy(seq.data)
            count_odd = 0
            for elem in s:
                if elem % 2 == 1:
                    count_odd += 1
            if count_odd % 2 == 1:
                return False
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
                for i in range(1, s[0] + 1):
                    s[i] += - 1
                del s[0]
        else:
            print("Passed argument is an empty sequence.")
    else:
        print("Passed argument is not a sequence.")
    return False


def get_degree_sequence_from_graph(g):
    if isinstance(g, Graph.Graph):
        s = Sequence()
        if g.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            if g.mode != "AM":
                convert_graph_representation(g, "AM")

            degree_seq_of_graph = [sum(elem) for elem in g.data]
            s.read_sequence_from_list(degree_seq_of_graph)
        return s
    else:
        print("Passed argument is not a graph.")


def construct_graph_from_degree_sequence(seq):
    g = Graph.Graph()
    if isinstance(seq, Sequence):
        if is_degree_sequence(seq):
            n = len(seq)

            g.mode = "AM"
            g.data = [[0] * n for _ in range(n)]
            my = [[i, seq[i]] for i in range(n)]

            second_list_argument = lambda li: li[1]

            while True:
                my.sort(key=second_list_argument, reverse=True)
                if my[0][1] == 0:
                    break
                for j in range(1, my[0][1]+1):
                    my[j][1] -= 1
                    g.data[my[0][0]][my[j][0]] = g.data[my[j][0]][my[0][0]] = 1
                del my[0]
        else:
            print("Passed sequence is not a degree sequence of a graph.")
    else:
        print("Passed argument is not a sequence.")
    return g
