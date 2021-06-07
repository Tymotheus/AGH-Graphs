from src.objects import *
from src.algorithms import *
from src.algorithms.strong_connectivity import construct_strongly_connected_digraph
from time import time

# g = Graph.Graph()
# print(g)
# GraphManager.convert_graph_representation(g, "AL")
# print(g)

g1 = Graph.Graph("example_data/proj1_am.txt")
print(g1, '\n')

g2 = Graph.Graph("example_data/proj1_im.txt", "IM")
print(g2, '\n')

g3 = GraphManager.GraphManager.make_random_graph_probability(12, 0.7)
print(g3, '\n')

wg1 = WeightedGraph.WeightedGraph("example_data/proj3b_am.txt")
print(wg1, '\n')

dg1 = Digraph.Digraph(file_path="example_data/proj4_digraph1.txt")
print(dg1, '\n')

wdg1 = WeightedDigraphManager.WeightedDigraphManager.construct_strongly_connected_weighted_digraph_probability(5, 0.3, -5, 10)
print(wdg1, '\n')

fn2 = FlowNetwork.FlowNetwork('example_data/proj5_flow_network_yes_not_equal_layers.txt', layers=[3, 3, 2])
print(fn2)