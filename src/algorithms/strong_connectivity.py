from random import randint, random

from src.objects.Digraph import Digraph
from src.objects.DigraphManager import DigraphManager


def kosaraju(dg):
    """
    Implementation of Kosaraju algorithm on a Digraph object.
    :param dg: Digraph object
    :return: list of lists of vertices in the same strong component
    """
    if not isinstance(dg, Digraph):
        print("Passed argument is not a digraph.")
        return
    n = len(dg.data)

    d = [[i, -1] for i in range(n)]
    f = [[i, -1] for i in range(n)]
    t = [0]

    for v in range(n):
        if d[v][1] == -1:
            dfs_time(dg, n, v, d, f, t)

    dg_T = DigraphManager.construct_transpose_digraph_from_digraph(dg)
    nr = 0
    comp = [-1 for _ in range(n)]
    f.sort(key=lambda li: li[1], reverse=True)

    for v in f:
        if comp[v[0]] == -1:
            nr = nr+1
            comp[v[0]] = nr
            components_r(dg_T, n, v[0], nr, comp)

    vertices_in_comps = [[] for _ in range(max(comp))]
    for i in range(n):
        vertices_in_comps[comp[i]-1].append(i)

    return vertices_in_comps


def dfs_time(digraph, n, v, d, f, t):
    """
    Auxiliary function used during Kosaraju algorithm to set the time of vertex consideration using DFS.
    :param digraph: Digraph object
    :param n: order of digraph
    :param v: considered vertex
    :param d: list of starting time consideration of vertices
    :param f: list of finish time consideration of vertices
    :param t: time of consideration
    :return: None
    """
    t[0] += 1
    d[v][1] = t[0]
    for u in range(n):
        if digraph.data[v][u] is not None:
            if d[u][1] == -1:
                dfs_time(digraph, n, u, d, f, t)
    t[0] += 1
    f[v][1] = t[0]


def components_r(digraph_T, n, v, nr, comp):
    """
    Auxiliary function used during Kosaraju algorithm to set the strong components.
    :param digraph_T: Digraph object
    :param n: order of digraph_T
    :param v: considered vertex
    :param nr: number of component
    :param comp: list of components assignment to vertices
    :return: None
    """
    for u in range(n):
        if digraph_T.data[v][u] is not None:
            if comp[u] == -1:
                comp[u] = nr
                components_r(digraph_T, n, u, nr, comp)


def tarjan(dg, root=0):
    """
    Modified implementation of tarjan algorithm which allows to create strongly connected digraphs.
    :param dg:Digraph object
    :param root: starting vertex
    :return: None
    """
    if not isinstance(dg, Digraph):
        print("Passed argument is not a digraph.")
        return

    n = len(dg.data)

    start_time = [-1 for _ in range(n)]
    low = [-1 for _ in range(n)]
    t = [0]

    dfs_tarjan(dg, n, root, start_time, t, low)


def dfs_tarjan(graph, n, i, start_time, t, low):
    """
    Auxiliary function used during modified Tarjan algorithm.
    :param graph: Digraph object
    :param n: order of graph
    :param i: considered vertex
    :param start_time: list of starting times of vertices consideration
    :param t: time of vertex consideration
    :param low: list of lowest times of vertices consideration
    :return: None
    """
    start_time[i] = t[0]
    low[i] = start_time[i]
    t[0] += 1
    for j in range(n):
        if graph.data[i][j] is not None:
            if start_time[j] == -1:
                dfs_tarjan(graph, n, j, start_time, t, low)
                low[i] = min(low[i], low[j], start_time[j])

    if low[i] == start_time[i]:
        x = randint(start_time[i], t[0]-1)
        y = randint(0, max(0, start_time[i]-1))
        v = None
        w = None
        for j in range(n):
            if start_time[j] == x:
                v = j
            if start_time[j] == y:
                w = j
        graph.data[v][w] = 1
        low[i] = y


def construct_strongly_connected_digraph(n, p, show_info=True):
    """
    Function creating strongly connected digraph.
    :param n: order of digraph
    :param p: probability of edge existence
    :param show_info: boolean whether to show creating information or not
    :return: strongly connected Digraph object
    """

    if n < 1:
        print("Random digraph cannot be created - number of vertices should be greater than 0.")
        return
    if p < 0 or p > 1:
        print("Random digraph cannot be created - probability should be between 0 and 1.")
        return

    dg = Digraph()
    dg.data = [[None] * n for _ in range(n)]

    tree = []
    vertices_to_tree = [i for i in range(n)]

    r = randint(0, n-1)
    tree.append(r)
    vertices_to_tree.remove(r)
    while len(vertices_to_tree):
        v = vertices_to_tree[randint(0, len(vertices_to_tree)-1)]
        vt = tree[randint(0, len(tree) - 1)]
        dg.data[vt][v] = 1
        tree.append(v)
        vertices_to_tree.remove(v)

    # res_before = kosaraju(dg)

    tarjan(dg, r)

    # res_after = kosaraju(dg)

    # print(res_before)
    # print(res_after)

    for i in range(n):
        for j in range(n):
            if not dg.data[i][j]:
                if random() <= p:
                    dg.data[i][j] = 1
        dg.data[i][i] = None

    if show_info is True:
        print("Random digraph has been created (Gilbert model: n = " + str(n) + ", p = " + "{:.3f}".format(p) + ").")
        print("Digraph represented by adjacency matrix.")
    return dg
