import copy

from src.objects.Sequence import Sequence
import src.objects.Graph as Graph
from src.objects.Stack import Stack

from src.algorithms.degree_sequences import construct_graph_from_degree_sequence, is_degree_sequence
from src.algorithms.connectivity import get_components_of_graph
from random import randrange


def is_graph_eulerian(g):
    if isinstance(g, Graph.Graph):
        if g.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            # IS COMPOSED OF MAXIMUM ONE COMPONENT WHICH IS NOT ISOLATED VERTEX
            components = get_components_of_graph(g)
            number_of_nontrivial_components = 0
            for component in components:
                if len(component) > 1:
                    number_of_nontrivial_components += 1
            if number_of_nontrivial_components == 0:
                return True
            elif number_of_nontrivial_components > 1:
                return False
            # EVEN DEGREES OF VERTICES
            for i in range(len(g.data)):
                if sum(g.data[i]) % 2 != 0:
                    return False
            return True
    else:
        print("Passed argument is not a graph.")
        return False


def construct_eulerian_graph(n):
    while True:
        even_degree_list = [randrange(0, n, 2) for _ in range(n)]
        # print(even_degree_list)
        seq = Sequence(even_degree_list)
        if is_degree_sequence(seq) is True:
            break
    g = construct_graph_from_degree_sequence(seq)
    while is_graph_eulerian(g) is False:
        g.randomize()
    return g


def get_eulerian_cycle_of_graph(g, show_cycle=True):
    eulerian_cycle = []
    if isinstance(g, Graph.Graph):
        if g.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            if is_graph_eulerian(g) is True:
                g_copy = copy.deepcopy(g)
                n = len(g_copy.data)
                stk_tmp = Stack()   # AUXILIARY STACK
                ec_stk = Stack()    # EULERIAN CYCLE STACK

                # ADD FIRST VERTEX OF EULERIAN CYCLE
                for i in range(1, n):
                    for j in range(0, i):
                        if g_copy.data[i][j] == 1:
                            stk_tmp.push(j)
                            break
                    else:
                        continue
                    break

                while stk_tmp.is_empty() is False:
                    v = stk_tmp.peek()
                    u = 0
                    while u < n:
                        if g_copy.data[v][u] == 1:
                            stk_tmp.push(u)
                            g_copy.data[v][u] = g_copy.data[u][v] = 0
                            break
                        u += 1
                    if u == n:
                        stk_tmp.pop()
                        ec_stk.push(v)

                eulerian_cycle = ec_stk.unpack_to_list()
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
