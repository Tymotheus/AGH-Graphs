import copy

from random import randrange

from src.objects.Sequence import Sequence
from src.objects.Stack import Stack
from src.objects.Graph import Graph
from src.objects.GraphManager import GraphManager

from src.algorithms.degree_sequences import construct_graph_from_degree_sequence, is_degree_sequence
from src.algorithms.connectivity import get_components_of_graph
from src.algorithms.representation_conversions import convert_graph_representation


def is_graph_eulerian(graph):
    """Returns True whether passed graph is eulerian and False otherwise.
        graph - Graph object"""

    if isinstance(graph, Graph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            if graph.representation != "AM":
                convert_graph_representation(graph, "AM")
            # IS COMPOSED OF MAXIMUM ONE COMPONENT WHICH IS NOT ISOLATED VERTEX
            components = get_components_of_graph(graph)
            number_of_nontrivial_components = 0
            for component in components:
                if len(component) > 1:
                    number_of_nontrivial_components += 1
            if number_of_nontrivial_components == 0:
                return True
            elif number_of_nontrivial_components > 1:
                return False
            # EVEN DEGREES OF VERTICES
            for i in range(len(graph.data)):
                if sum(graph.data[i]) % 2 != 0:
                    return False
            return True
    else:
        print("Passed argument is not a graph.")
        return False


def construct_eulerian_graph(n):
    """Returns an eulerian graph.
        n - number of vertices"""

    while True:
        even_degree_list = [randrange(0, n, 2) for _ in range(n)]
        # print(even_degree_list)
        seq = Sequence(even_degree_list)
        if is_degree_sequence(seq) is True:
            break
    graph = construct_graph_from_degree_sequence(seq)
    while is_graph_eulerian(graph) is False:
        GraphManager.randomize(graph)
    return graph


def get_eulerian_cycle_of_graph(graph, show_cycle=True):
    """Returns list of vertices which form an eulerian cycle of a graph.
        graph - Graph object, should be eulerian
        show_cycle - boolean whether to show found cycle"""

    eulerian_cycle = []
    if isinstance(graph, Graph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            if is_graph_eulerian(graph) is True:
                if graph.representation != "AM":
                    convert_graph_representation(graph, "AM")
                g_copy = copy.deepcopy(graph)
                n = len(g_copy.data)
                tmp_stack = Stack()   # AUXILIARY STACK
                ec_stack = Stack()    # EULERIAN CYCLE STACK

                # ADD FIRST VERTEX OF EULERIAN CYCLE
                for i in range(1, n):
                    for j in range(0, i):
                        if g_copy.data[i][j] == 1:
                            tmp_stack.push(j)
                            break
                    else:
                        continue
                    break

                while tmp_stack.is_empty() is False:
                    v = tmp_stack.peek()
                    u = 0
                    while u < n:
                        if g_copy.data[v][u] == 1:
                            tmp_stack.push(u)
                            g_copy.data[v][u] = g_copy.data[u][v] = 0
                            break
                        u += 1
                    if u == n:
                        tmp_stack.pop()
                        ec_stack.push(v)

                eulerian_cycle = ec_stack.unpack_to_list()
                if show_cycle is True and len(eulerian_cycle) > 0:
                    print("Eulerian cycle of graph:\n" + str(eulerian_cycle[0]+1), end='')
                    for i in range(1, len(eulerian_cycle)):
                        print(" -> " + str(eulerian_cycle[i]+1), end='')
                    print()
            else:
                print("Passed graph is not a eulerian.")
    else:
        print("Passed argument is not a graph.")
    return eulerian_cycle
