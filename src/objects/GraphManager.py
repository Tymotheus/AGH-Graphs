from random import random, sample, uniform

from src.objects.Graph import Graph

from src.algorithms.representation_conversions import convert_graph_representation


class GraphManager:
    """Representation of a simple graph manager which allows to execute some operations connected with simple graphs."""

    def __init__(self):
        """GraphManager constructor. Simply prints that an instance of the GraphManger have been created."""

        print("GraphManager has been created")

    @staticmethod
    def make_random_graph_edge_number(n, m, show_info=True):
        """Creates and return a graph with random number of edges and vertices (Erdos-Renyi model).
        n - number of vertices
        m - number of edges, cannot be greater than n * (n-1) / 2
        show_info - boolean whether to print information about the graph after its creation."""

        max_num_of_edges = n * (n-1) / 2
        if m < 0 or m > max_num_of_edges:
            print("Random graph cannot be created - number of edges should be between 0 and n*(n-1)/2.")
            return
        g = Graph()
        g.representation = 'AM'
        g.data = [[0] * n for _ in range(n)]
        indexes_of_existing_edges = sample(range(0, int(max_num_of_edges)), m)
        index = 0
        for i in range(1, n):
            for j in range(0, i):
                if index in indexes_of_existing_edges:
                    g.data[i][j] = g.data[j][i] = 1
                index = index+1
        if show_info is True:
            print("Random graph has been created (Erdos-Renyi model: n = " + str(n) + ", m = " + str(m) + ").")
            print("Graph represented by adjacency matrix.")
        return g

    @staticmethod
    def make_random_graph_probability(n, p, show_info=True):
        """Creates a random graph for given probability of edge existence (Gilbert model).
        n - number of vertices
        p - probability with which each edge occurs independently, must be between 0 and 1
        show_info - boolean whether to print information about the graph after its creation."""

        if p < 0 or p > 1:
            print("Random graph cannot be created - probability should be between 0 and 1.")
            return

        g = Graph()
        g.representation = 'AM'
        g.data = [[0] * n for _ in range(n)]
        for i in range(1, n):
            for j in range(0, i):
                if random() <= p:
                    g.data[i][j] = g.data[j][i] = 1
        if show_info is True:
            print("Random graph has been created (Gilbert model: n = " + str(n) + ", p = " + "{:.3f}".format(p) + ").")
            print("Graph represented by adjacency matrix.")
        return g

    @staticmethod
    def randomize(graph, show_shuffling_statistics=False):
        """Shuffles edges between vertices in the given graph.
        g - Graph object
        show_shuffling_statistics - boolean whether to print information about the randomization process."""

        if not isinstance(graph, Graph):
            print("Passed argument is not a graph.")
            return
        if graph.data is None:
            print("Graph is empty (no data) - cannot shuffle edges.")
            return
        if graph.representation != "AM":
            convert_graph_representation(graph, "AM")
        n = len(graph.data)
        list_of_edges = []
        for i in range(1, n):
            for j in range(0, i):
                if graph.data[i][j] == 1:
                    list_of_edges.append([i, j])
        m = len(list_of_edges)
        number_of_iterations_arr = []
        exceeded = 0
        number_of_shuffles = int(0.5 * m)
        for i in range(number_of_shuffles):
            flag_shuffled = False
            number_of_iterations = 0
            max_iterations = int(uniform(2, 4) * m)
            while flag_shuffled is False and number_of_iterations < max_iterations:
                first_edge_index, second_edge_index = sample(range(0, m), 2)
                first_edge = list_of_edges[first_edge_index]
                second_edge = list_of_edges[second_edge_index]
                if first_edge[0] != second_edge[0] and first_edge[0] != second_edge[1] and first_edge[1] != second_edge[0] and first_edge[1] != second_edge[1]:
                    if graph.data[first_edge[0]][second_edge[1]] == 0 and first_edge[0] != second_edge[1] and graph.data[second_edge[0]][first_edge[1]] == 0 and second_edge[0] != first_edge[1]:
                        graph.data[first_edge[0]][second_edge[1]] = graph.data[second_edge[0]][first_edge[1]] = graph.data[second_edge[1]][first_edge[0]] = graph.data[first_edge[1]][second_edge[0]] = 1
                        graph.data[first_edge[0]][first_edge[1]] = graph.data[second_edge[0]][second_edge[1]] = graph.data[first_edge[1]][first_edge[0]] = graph.data[second_edge[1]][second_edge[0]] = 0
                        list_of_edges.append([first_edge[0], second_edge[1]] if first_edge[0] > second_edge[1] else [second_edge[1], first_edge[0]])
                        list_of_edges.append([second_edge[0], first_edge[1]] if second_edge[0] > first_edge[1] else [first_edge[1], second_edge[0]])
                        list_of_edges.pop(first_edge_index if first_edge_index > second_edge_index else second_edge_index)
                        list_of_edges.pop(second_edge_index if first_edge_index > second_edge_index else first_edge_index)
                        flag_shuffled = True
                    elif graph.data[first_edge[0]][second_edge[0]] == 0 and first_edge[0] != second_edge[0] and graph.data[second_edge[1]][first_edge[1]] == 0 and second_edge[1] != first_edge[1]:
                        graph.data[first_edge[0]][second_edge[0]] = graph.data[second_edge[1]][first_edge[1]] = graph.data[second_edge[0]][first_edge[0]] = graph.data[first_edge[1]][second_edge[1]] = 1
                        graph.data[first_edge[0]][first_edge[1]] = graph.data[second_edge[0]][second_edge[1]] = graph.data[first_edge[1]][first_edge[0]] = graph.data[second_edge[1]][second_edge[0]] = 0
                        list_of_edges.append([first_edge[0], second_edge[0]] if first_edge[0] > second_edge[0] else [second_edge[0], first_edge[0]])
                        list_of_edges.append([second_edge[1], first_edge[1]] if second_edge[1] > first_edge[1] else [first_edge[1], second_edge[1]])
                        list_of_edges.pop(first_edge_index if first_edge_index > second_edge_index else second_edge_index)
                        list_of_edges.pop(second_edge_index if first_edge_index > second_edge_index else first_edge_index)
                        flag_shuffled = True
                number_of_iterations += 1
                if number_of_iterations >= 3*m:
                    exceeded += 1
            number_of_iterations_arr.append(number_of_iterations)
        if show_shuffling_statistics:
            print("Shuffled edges of a graph " + str(number_of_shuffles) + " times.")
            print("n: " + str(n) + ", m: " + str(m) + ", average: " + str(sum(number_of_iterations_arr)/len(number_of_iterations_arr)) + ", exceeded: " + str(exceeded))
