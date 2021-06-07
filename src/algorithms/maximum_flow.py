import math

from src.objects.FlowNetwork import FlowNetwork
from src.objects.FlowNetworkManager import FlowNetworkManager


def ford_fulkerson(fn):
    """
    Implementation of Ford-Fulkerson algorithm on a FlowNetwork object.
        After call, current flow in passed FlowNetwork object is set to the maximum flow found during algorithm execution.
    :param fn: FlowNetwork object
    :return: value of maximum flow in flow network
    """

    if not isinstance(fn, FlowNetwork):
        print("Passed argument is not a flow network.")
        return
    n = len(fn.data)
    for i in range(n):
        for j in range(n):
            fn.data[i][j][0] = 0

    p = []
    while bfs_maximum_flow_augmenting_path(FlowNetworkManager.get_residual_network_of_flow_network(fn), n, p):
        c_f_min = p[0][2]
        for i in range(1, len(p)):
            if c_f_min > p[i][2]:
                c_f_min = p[i][2]
        for edge in p:
            if fn.data[edge[0]][edge[1]][1]:
                if fn.data[edge[0]][edge[1]][1] - fn.data[edge[0]][edge[1]][0] >= c_f_min:
                    fn.data[edge[0]][edge[1]][0] += c_f_min
                else:
                    fn.data[edge[0]][edge[1]][0] -= c_f_min
        p = []

    s_out = 0
    t_in = 0
    for i in range(n):
        s_out += fn.data[0][i][0]
        t_in += fn.data[i][n-1][0]
    if s_out == t_in:
        return t_in


def bfs_maximum_flow_augmenting_path(wd, n, p):
    """
    Function looking for a path between first and last vertices. It is based in BFS algorithm.
    It is used to find an augmenting path in residual network.
    :param wd: WeightedDigraph object
    :param n: number of vertices
    :param p: path between first and last vertices. Each element is of form [v,u,w(v,u)] where:
        u, v - vertices which creates an arc in an augmenting path (in residual network)
        w(v,u) - capacity of u-v arc in residual network
    :return: length of an augmenting path.
        If the length is equal to 0, an augmenting path does not exist.
    """

    d_s = [math.inf for _ in range(n)]
    p_s = [None for _ in range(n)]
    d_s[0] = 0

    queue = [0]

    while len(queue):
        v = queue.pop(0)
        for u in range(n):
            if wd.data[v][u]:
                if d_s[u] is math.inf:
                    d_s[u] = d_s[v] + 1
                    p_s[u] = v
                    queue.append(u)
        if p_s[n-1] is not None:
            break

    if p_s[n-1] is not None:
        v = n - 1
        while v != 0:
            u = p_s[v]
            p.append([u, v, wd.data[u][v]])
            v = p_s[v]

        p.reverse()

    return len(p)
