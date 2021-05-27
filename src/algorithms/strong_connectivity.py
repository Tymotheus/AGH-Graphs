from random import randint, random

from src.objects.Digraph import Digraph
from src.objects.DigraphManager import DigraphManager


def kosaraju(dg):
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

    return comp


def dfs_time(graph, n, v, d, f, t):
    t[0] += 1
    d[v][1] = t[0]
    for u in range(n):
        if graph.data[v][u]:
            if d[u][1] == -1:
                dfs_time(graph, n, u, d, f, t)
    t[0] += 1
    f[v][1] = t[0]


def components_r(graph, n, v, nr, comp):
    for u in range(n):
        if graph.data[v][u]:
            if comp[u] == -1:
                comp[u] = nr
                components_r(graph, n, u, nr, comp)


def tarjan(dg, root=0):
    if not isinstance(dg, Digraph):
        print("Passed argument is not a digraph.")
        return

    n = len(dg.data)

    start_time = [-1 for _ in range(n)]
    low = [-1 for _ in range(n)]
    t = [0]

    dfs_tarjan(dg, n, root, start_time, t, low)


def dfs_tarjan(graph, n, i, start_time, t, low):
    start_time[i] = t[0]
    low[i] = start_time[i]
    t[0] += 1
    for j in range(n):
        if graph.data[i][j]:
            if start_time[j] == -1:
                dfs_tarjan(graph, n, j, start_time, t, low)
                low[i] = min(low[i], low[j], start_time[j])

    if low[i] == start_time[i]:
        # print("st=%s\tgt=%s" %(start_time[i], t[0]))
        x = randint(start_time[i], t[0]-1)
        y = randint(0, max(0, start_time[i]-1))
        # print("x=%s, y=%s" % (x, y))
        v = None
        w = None
        for j in range(n):
            if start_time[j] == x:
                v = j
            if start_time[j] == y:
                w = j
        # print("v=%s, w=%s" % (v, w))
        graph.data[v][w] = 1
        low[i] = y


def construct_strongly_connected_digraph(n, p, show_info=True):
    """

    :param n:
    :param p:
    :param show_info:
    :return:
    """

    if n < 1:
        print("Random digraph cannot be created - number of vertices should be greater than 0.")
        return
    if p < 0 or p > 1:
        print("Random digraph cannot be created - probability should be between 0 and 1.")
        return

    dg = Digraph()
    dg.data = [[0] * n for _ in range(n)]

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

    res_before = kosaraju(dg)

    tarjan(dg, r)

    res_after = kosaraju(dg)

    print(res_before)
    print(res_after)
    # print(dg)

    for i in range(n):
        for j in range(n):
            if not dg.data[i][j]:
                if random() <= p:
                    dg.data[i][j] = 1
    for i in range(n):
        dg.data[i][i] = 0

    if show_info is True:
        print("Random digraph has been created (Gilbert model: n = " + str(n) + ", p = " + "{:.3f}".format(p) + ").")
        print("Digraph represented by adjacency matrix.")
    return dg
