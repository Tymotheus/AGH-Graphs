import src.objects.Graph as Graph
from src.objects.Stack import Stack

from src.algorithms.representation_conversions import convert_graph_representation
from src.algorithms.connectivity import is_graph_connected


def get_hamiltonian_cycle_of_graph(g, show_cycle=True):
    hamiltonian_cycle = []
    if isinstance(g, Graph.Graph):
        if g.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            if g.mode != "AM":
                convert_graph_representation(g, "AM")
            if is_graph_connected(g) is True:
                n = len(g.data)
                vertices_visited = [0 for _ in range(n)]
                hc_stk = Stack()  # HAMILTONIAN CYCLE STACK

                # ADD FIRST VERTEX OF HAMILTONIAN CYCLE
                if n >= 3:
                    for v in range(n):
                        if vertices_visited[v] == 0:
                            vertices_visited[v] = 1
                            hc_stk.push(v)
                            hamiltonian_dfs_recursive(g, hc_stk, v, n, vertices_visited, v)
                            if len(hc_stk) == n and g.data[v][hc_stk.peek()] == 1:
                                hc_stk.push(v)
                                break
                            vertices_visited[v] = 0
                            hc_stk.pop()
                if hc_stk.is_empty():
                    print("Passed graph does not have a hamiltonian cycle.")
                else:
                    hamiltonian_cycle = hc_stk.unpack_to_list()
                    if show_cycle is True and len(hamiltonian_cycle) > 0:
                        print("Hamiltonian cycle of graph:\n" + str(hamiltonian_cycle[0]+1), end='')
                        for i in range(1, len(hamiltonian_cycle)):
                            print(" -> " + str(hamiltonian_cycle[i]+1), end='')
                        print()
            else:
                print("Passed graph is not connected.")
    else:
        print("Passed argument is not a graph.")
    return hamiltonian_cycle


def hamiltonian_dfs_recursive(g, hc_stk, v0, n, vertices_visited, v=0):
    if g.mode != "AM":
        convert_graph_representation(g, "AM")
    for u in range(n):
        if g.data[v][u] == 1:
            if vertices_visited[u] == 0:
                vertices_visited[u] = 1
                hc_stk.push(u)
                hamiltonian_dfs_recursive(g, hc_stk, v0, n, vertices_visited, u)
                if len(hc_stk) == n and g.data[v0][hc_stk.peek()] == 1:
                    break
                vertices_visited[u] = 0
                hc_stk.pop()


def get_hamiltonian_cycle_of_graph_opt(g, show_cycle=True):
    hamiltonian_cycle = []
    if isinstance(g, Graph.Graph):
        if g.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            if g.mode != "AM":
                convert_graph_representation(g, "AM")
            if is_graph_connected(g) is True:
                n = len(g.data)
                vertices_visited = [[i, sum(g.data[i]), 0] for i in range(n)]   # index, degree, visited
                hc_stk = Stack()  # HAMILTONIAN CYCLE STACK
                second_list_argument = lambda li: li[1]
                vertices_visited.sort(key=second_list_argument, reverse=True)

                # ADD FIRST VERTEX OF HAMILTONIAN CYCLE
                if n >= 3:
                    for v in vertices_visited:
                        if v[2] == 0:
                            v[2] = 1
                            hc_stk.push(v[0])
                            hamiltonian_dfs_recursive_opt(g, hc_stk, v[0], n, vertices_visited, v[0])
                            if len(hc_stk) == n and g.data[v[0]][hc_stk.peek()] == 1:
                                hc_stk.push(v[0])
                                break
                            v[2] = 0
                            hc_stk.pop()
                if hc_stk.is_empty():
                    print("Passed graph does not have a hamiltonian cycle.")
                else:
                    hamiltonian_cycle = hc_stk.unpack_to_list()
                    if show_cycle is True and len(hamiltonian_cycle) > 0:
                        print("Hamiltonian cycle of graph:\n" + str(hamiltonian_cycle[0]+1), end='')
                        for i in range(1, len(hamiltonian_cycle)):
                            print(" -> " + str(hamiltonian_cycle[i]+1), end='')
                        print()
            else:
                print("Passed graph is not connected.")
    else:
        print("Passed argument is not a graph.")
    return hamiltonian_cycle


def hamiltonian_dfs_recursive_opt(g, hc_stk, v0, n, vertices_visited, v=0):
    if g.mode != "AM":
        convert_graph_representation(g, "AM")
    for u in range(n-1, -1, -1):
        if g.data[v][vertices_visited[u][0]] == 1:
            if vertices_visited[u][2] == 0:
                vertices_visited[u][2] = 1
                hc_stk.push(vertices_visited[u][0])
                hamiltonian_dfs_recursive_opt(g, hc_stk, v0, n, vertices_visited, vertices_visited[u][0])
                if len(hc_stk) == n and g.data[v0][hc_stk.peek()] == 1:
                    break
                vertices_visited[u][2] = 0
                hc_stk.pop()
