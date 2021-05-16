from src.objects.GraphManager import GraphManager
from src.objects.Graph import Graph
from src.algorithms.representation_conversions import convert_graph_representation

print("\n\n---------------------------------------- AD. 1.1 ----------------------------------------")

# READING FROM FILE
g1 = Graph("example_data/proj1_am.txt")
print(g1)
g1.draw()

g2 = Graph("example_data/proj1_im.txt", 'IM')
print(g2)
convert_graph_representation(g2, "AM")
g2.draw()

g3 = Graph("example_data/proj1_al.txt", 'AL')
print(g3)
convert_graph_representation(g3, "AM")
g3.draw()

# CONVERSIONS
convert_graph_representation(g3, "IM")   # AL -> IM
print(g3)
convert_graph_representation(g3, "AL")   # IM -> AL
print(g3)
convert_graph_representation(g3, "AM")   # AL -> AM
print(g3)
convert_graph_representation(g3, "IM")   # AM -> IM
print(g3)
convert_graph_representation(g3, "AM")   # IM -> AM
print(g3)
convert_graph_representation(g3, "AL")   # AM -> AL
print(g3)

print("\n\n---------------------------------------- AD. 1.2 ----------------------------------------")

# DRAWING A GRAPH
convert_graph_representation(g3, "AM")
g3.draw()

print("\n\n---------------------------------------- AD. 1.3 ----------------------------------------")

# RANDOM GRAPH - ERDOS-RENYI MODEL BASED ON NUMBER OF EDGES
g_ER = GraphManager.make_random_graph_edge_number(17, 21)
print(g_ER)
g_ER.draw()

# RANDOM GRAPH - GILBERT MODEL BASED ON PROBABILITY OF EDGE OCCURRENCE
g_G = GraphManager.make_random_graph_probability(100, 0.03)
print(g_G)
g_G.draw()
