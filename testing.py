from src.objects import *
from src.algorithms import *
from src.algorithms.strong_connectivity import construct_strongly_connected_digraph
from time import time

g = Graph.Graph()
print(g)
GraphManager.convert_graph_representation(g, "AL")
print(g)