from src.objects.Graph import Graph
from src.objects.WeightedGraphManager import WeightedGraphManager

from src.algorithms.connectivity import construct_connected_graph_edge_number, construct_connected_graph_probability


print("\n\n---------------------------------------- AD. 3.1 ----------------------------------------")

# CONNECTED WEIGHTED GRAPH USING PRUFER CODE AND ERDOS-RENYI MODEL
g1 = construct_connected_graph_edge_number(5, 6)
g1.draw()
wg1 = WeightedGraphManager.make_weighted_graph_from_simple_graph(g1)
wg1.draw()

# CONNECTED WEIGHTED GRAPH USING PRUFER CODE AND GILBERT MODEL
g2 = construct_connected_graph_probability(5, 0.5)
g2.draw()
wg2 = WeightedGraphManager.make_weighted_graph_from_simple_graph(g2)
wg2.draw()

print("\n\n---------------------------------------- AD. 3.2 ----------------------------------------")


print("\n\n---------------------------------------- AD. 3.3 ----------------------------------------")


print("\n\n---------------------------------------- AD. 3.4 ----------------------------------------")


print("\n\n---------------------------------------- AD. 3.5 ----------------------------------------")
