import src.objects.Graph as Graph
from src.objects.Stack import Stack

from src.algorithms.representation_conversions import convert_graph_representation
from src.algorithms.connectivity import is_graph_connected


def get_hamiltonian_cycle_of_graph(graph, show_cycle=True):
    """Returns list of vertices which form a hamiltonian cycle of a graph.
        graph - Graph object
        show_cycle - boolean whether to show found cycle"""

    hamiltonian_cycle = []
    if isinstance(graph, Graph.Graph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            if graph.representation != "AM":
                convert_graph_representation(graph, "AM")
            if is_graph_connected(graph) is True:
                n = len(graph.data)
                v_visited = [False for _ in range(n)]
                hc_stack = Stack()  # HAMILTONIAN CYCLE STACK

                # ADD FIRST VERTEX OF HAMILTONIAN CYCLE
                if n >= 3:
                    for v in range(n):
                        if v_visited[v] is False:
                            v_visited[v] = True
                            hc_stack.push(v)
                            hamiltonian_dfs_recursive(graph, hc_stack, v, n, v_visited, v)
                            if len(hc_stack) == n and graph.data[v][hc_stack.peek()] is not None:
                                hc_stack.push(v)
                                break
                            v_visited[v] = False
                            hc_stack.pop()
                if hc_stack.is_empty():
                    print("Passed graph does not have a hamiltonian cycle.")
                else:
                    hamiltonian_cycle = hc_stack.unpack_to_list()
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


def hamiltonian_dfs_recursive(graph, hc_stack, v0, n, v_visited, v=0):
    """Recursive function of obtaining a hamiltonian cycle.
        graph - Graph object
        hc_stack - hamiltonian cycle stack
        v0 - considered vertex
        n - number of vertices
        v_visited - list of information whether a vertex was visited or not
        v - vertex to consider"""

    if graph.representation != "AM":
        convert_graph_representation(graph, "AM")
    for u in range(n):
        if graph.data[v][u] is not None:
            if v_visited[u] is False:
                v_visited[u] = True
                hc_stack.push(u)
                hamiltonian_dfs_recursive(graph, hc_stack, v0, n, v_visited, u)
                if len(hc_stack) == n and graph.data[v0][hc_stack.peek()] is not None:
                    break
                v_visited[u] = False
                hc_stack.pop()


def get_hamiltonian_cycle_of_graph_optimized(graph, show_cycle=True):
    """Returns list of vertices which form a hamiltonian cycle of a graph. Optimized function using S. Martello approach.
        graph - Graph object
        show_cycle - boolean whether to show found cycle"""

    hamiltonian_cycle = []
    if isinstance(graph, Graph.Graph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot obtain it's degree sequence.")
        else:
            if graph.representation != "AM":
                convert_graph_representation(graph, "AM")
            if is_graph_connected(graph) is True:
                n = len(graph.data)
                v_and_d_and_visited = []
                for i in range(n):
                    v_degree = 0
                    for item in graph.data[i]:
                        if item is not None:
                            v_degree += 1
                    v_and_d_and_visited.append([i, v_degree, False]) # index, degree, visited
                hc_stack = Stack()  # HAMILTONIAN CYCLE STACK
                v_and_d_and_visited.sort(key=lambda li: li[1], reverse=True)

                # ADD FIRST VERTEX OF HAMILTONIAN CYCLE
                if n >= 3:
                    for v in v_and_d_and_visited:
                        if v[2] is False:
                            v[2] = True
                            hc_stack.push(v[0])
                            hamiltonian_dfs_recursive_optimized(graph, hc_stack, v[0], n, v_and_d_and_visited, v[0])
                            if len(hc_stack) == n and graph.data[v[0]][hc_stack.peek()] == 1:
                                hc_stack.push(v[0])
                                break
                            v[2] = False
                            hc_stack.pop()
                if hc_stack.is_empty():
                    print("Passed graph does not have a hamiltonian cycle.")
                else:
                    hamiltonian_cycle = hc_stack.unpack_to_list()
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


def hamiltonian_dfs_recursive_optimized(graph, hc_stack, v0, n, v_and_d_and_visited, v=0):
    """Recursive function of obtaining a hamiltonian cycle for optimized function using S. Martello approach.
        graph - Graph object
        hc_stack - hamiltonian cycle stack
        v0 - considered vertex
        n - number of vertices
        v_and_d_and_visited - list of information whether a vertex was visited or not and it's degree
        v - vertex to consider"""

    if graph.representation != "AM":
        convert_graph_representation(graph, "AM")
    for u in range(n-1, -1, -1):
        if graph.data[v][v_and_d_and_visited[u][0]] == 1:
            if v_and_d_and_visited[u][2] is False:
                v_and_d_and_visited[u][2] = True
                hc_stack.push(v_and_d_and_visited[u][0])
                hamiltonian_dfs_recursive_optimized(graph, hc_stack, v0, n, v_and_d_and_visited,
                                                    v_and_d_and_visited[u][0])
                if len(hc_stack) == n and graph.data[v0][hc_stack.peek()] == 1:
                    break
                v_and_d_and_visited[u][2] = False
                hc_stack.pop()
