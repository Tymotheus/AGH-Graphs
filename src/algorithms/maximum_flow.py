import math

from src.objects.FlowNetwork import FlowNetwork
from src.objects.FlowNetworkManager import FlowNetworkManager


def ford_fulkerson(fn):
    """"Performs Ford-Fulkerson algorithm on a FlowNetwork object. In result current flow in passed flow network is modified to the maximum flow.
            fn - FlowNetwork object"""

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


def bfs_maximum_flow_augmenting_path(wd, n, p):

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
