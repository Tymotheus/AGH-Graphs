import src.objects.Graph as Graph
from src.algorithms.representation_check import *


def convert_from_AM_to_IM(g):
    n = len(g.data)
    m = 0
    for i in range(1, n):
        for j in range(0, i):
            m = m + g.data[i][j]
    new_data = [[0] * m for _ in range(n)]
    m_index = 0
    for i in range(1, n):
        for j in range(0, i):
            if g.data[i][j] == 1:
                new_data[i][m_index] = new_data[j][m_index] = 1
                m_index = m_index + 1
    g.data = new_data
    g.mode = "IM"


def convert_from_IM_to_AM(g):
    n = len(g.data)
    m = len(g.data[0])
    new_data = [[0] * n for _ in range(n)]
    for j in range(0, m):
        first_index = None
        for i in range(0, n):
            if g.data[i][j] == 1:
                if first_index is None:
                    first_index = i
                else:
                    new_data[first_index][i] = new_data[i][first_index] = 1
                    break
    g.data = new_data
    g.mode = "AM"


def convert_from_AM_to_AL(g):
    n = len(g.data)
    new_data = [[] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(0, i):
            if g.data[i][j] == 1:
                new_data[i].append(j+1)
                new_data[j].append(i+1)
    g.data = new_data
    g.mode = "AL"


def convert_from_AL_to_AM(g):
    n = len(g.data)
    new_data = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for neighbour in g.data[i]:
            new_data[i][neighbour-1] = new_data[neighbour-1][i] = 1
            g.data[neighbour-1].remove(i+1)
    g.data = new_data
    g.mode = "AM"


def convert_from_IM_to_AL(g):
    n = len(g.data)
    m = len(g.data[0])
    new_data = [[] * n for _ in range(n)]
    for j in range(0, m):
        first_index = None
        for i in range(0, n):
            if g.data[i][j] == 1:
                if first_index is None:
                    first_index = i
                else:
                    new_data[first_index].append(i+1)
                    new_data[i].append(first_index+1)
    g.data = new_data
    g.mode = "AL"


def convert_from_AL_to_IM(g):
    n = len(g.data)
    m = 0
    for v_list in g.data:
        m = m + len(v_list)
    m = int(m / 2)
    new_data = [[0] * m for _ in range(n)]
    m_index = 0
    for i in range(0, n):
        for neighbour in g.data[i]:
            new_data[i][m_index] = new_data[neighbour-1][m_index] = 1
            g.data[neighbour-1].remove(i+1)
            m_index = m_index + 1
    g.data = new_data
    g.mode = "IM"


conversion_map = {"AM_IM": convert_from_AM_to_IM,
                  "AM_AL": convert_from_AM_to_AL,
                  "IM_AM": convert_from_IM_to_AM,
                  "IM_AL": convert_from_IM_to_AL,
                  "AL_AM": convert_from_AL_to_AM,
                  "AL_IM": convert_from_AL_to_IM}


def convert_graph_representation(graph, new_representation):
    if isinstance(graph, Graph.Graph):
        if graph.data is None:
            print("Graph is empty (no data) - cannot convert it to any representation.")
            return
        key = graph.mode + "_" + new_representation
        if graph.mode == new_representation:
            print("Conversion is not needed.")
        elif conversion_map.get(key) is not None:
            if conversion_check_map[graph.mode](graph.data) is False:
                print("Cannot do a conversion - graph data is not of the form of it's representation.")
                return
            print("Graph representation is being changed from " + graph.mode + " to " + new_representation + ".")
            conversion_map[key](graph)
        else:
            print("Passed conversion from " + graph.mode + " to " + new_representation + " is unknown.")
    else:
        print("Passed argument is not a graph.")
