import src.objects.Graph as Graph
from src.algorithms.representation_checks import *


def convert_from_AM_to_IM(graph):
    """Converts the given graph with its data, from the Adjacency Matrix
    representation to Incidence Matrix representation."""

    n = len(graph.data)
    m = 0
    for i in range(1, n):  # i stands for a row
        for j in range(0, i):  # j stands for a column
            m = m + graph.data[i][j]
    new_data = [[0] * m for _ in range(n)]
    m_index = 0
    for i in range(1, n):
        for j in range(0, i):
            if graph.data[i][j] == 1:
                new_data[i][m_index] = new_data[j][m_index] = 1
                m_index = m_index + 1
    graph.data = new_data
    graph.representation = "IM"


def convert_from_IM_to_AM(graph):
    """Converts the given graph with its data, from the Incidence Matrix
    representation, to Adjacency Matrix representation."""

    n = len(graph.data)
    m = len(graph.data[0])
    new_data = [[0] * n for _ in range(n)]
    for j in range(0, m):
        first_index = None
        for i in range(0, n):
            if graph.data[i][j] == 1:
                if first_index is None:
                    first_index = i
                else:
                    new_data[first_index][i] = new_data[i][first_index] = 1
                    break
    graph.data = new_data
    graph.representation = "AM"


def convert_from_AM_to_AL(graph):
    """Converts the given graph with its data, from the Adjacency Matrix
    representation, to Adjacency List representation."""

    n = len(graph.data)
    new_data = [[] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(0, i):
            if graph.data[i][j] == 1:
                new_data[i].append(j+1)
                new_data[j].append(i+1)
    graph.data = new_data
    graph.representation = "AL"


def convert_from_AL_to_AM(graph):
    """Converts the given graph with its data, from the Adjacency List
    representation, to Adjacency Matrix representation."""

    n = len(graph.data)
    new_data = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for neighbour in graph.data[i]:
            new_data[i][neighbour-1] = new_data[neighbour-1][i] = 1
            graph.data[neighbour - 1].remove(i + 1)
    graph.data = new_data
    graph.representation = "AM"


def convert_from_IM_to_AL(graph):
    """Converts the given graph with its data, from the Incidence Matrix
    representation, to Adjacency List representation."""

    n = len(graph.data)
    m = len(graph.data[0])
    new_data = [[] * n for _ in range(n)]
    for j in range(0, m):
        first_index = None
        for i in range(0, n):
            if graph.data[i][j] == 1:
                if first_index is None:
                    first_index = i
                else:
                    new_data[first_index].append(i+1)
                    new_data[i].append(first_index+1)
    graph.data = new_data
    graph.representation = "AL"


def convert_from_AL_to_IM(graph):
    """Converts the given graph with its data, from the Adjacency List
    representation, to Incidence Matrix representation."""

    n = len(graph.data)
    m = 0
    for v_list in graph.data:
        m = m + len(v_list)
    m = int(m / 2)
    new_data = [[0] * m for _ in range(n)]
    m_index = 0
    for i in range(0, n):
        for neighbour in graph.data[i]:
            new_data[i][m_index] = new_data[neighbour-1][m_index] = 1
            graph.data[neighbour - 1].remove(i + 1)
            m_index = m_index + 1
    graph.data = new_data
    graph.representation = "IM"


"""Dictionary object that maps the representation strings
to their proper conversion functions."""
conversion_map = {"AM_IM": convert_from_AM_to_IM,
                  "AM_AL": convert_from_AM_to_AL,
                  "IM_AM": convert_from_IM_to_AM,
                  "IM_AL": convert_from_IM_to_AL,
                  "AL_AM": convert_from_AL_to_AM,
                  "AL_IM": convert_from_AL_to_IM}


def convert_graph_representation(graph, new_representation):
    """Checks the representation of a graph, and converts it to the representation
    passed as an argument, using proper conversion function."""
    
    if not isinstance(graph, Graph.Graph):
        print("Passed argument is not a graph.")
        return
    if graph.data is None:
        print("Graph is empty (no data) - cannot convert it to any representation.")
        return
    key = graph.representation + "_" + new_representation
    if graph.representation == new_representation:
        print("Conversion is not needed.")
    elif conversion_map.get(key) is not None:
        if conversion_check_map[graph.representation](graph.data) is False:
            print("Cannot do a conversion - graph data is not of the form of it's representation.")
            return
        print("Graph representation is being changed from " + graph.representation + " to " + new_representation + ".")
        conversion_map[key](graph)
    else:
        print("Passed conversion from " + graph.representation + " to " + new_representation + " is unknown.")
