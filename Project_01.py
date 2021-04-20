import os
from random import randrange, random

from src.objects.Graph import Graph
from src.algorithms.representation_conversions import convert_graph_representation

os.system('cls')

g = Graph()

print("\n\n---------------------------------------- AD. 1.1 ----------------------------------------")

# reading from file
g.read_graph_from_file("example_data/proj1_am.txt")
print(g)
g.draw(600, 600)

g.read_graph_from_file("example_data/proj1_im.txt", 'IM')
print(g)
convert_graph_representation(g, "AM")
g.draw(600, 600)

g.read_graph_from_file("example_data/proj1_al.txt", 'AL')
print(g)
convert_graph_representation(g, "AM")
g.draw(600, 600)

# conversions
convert_graph_representation(g, "IM")   # AL -> IM
print(g)
convert_graph_representation(g, "AL")   # IM -> AL
print(g)
convert_graph_representation(g, "AM")   # AL -> AM
print(g)
convert_graph_representation(g, "IM")   # AM -> IM
print(g)
convert_graph_representation(g, "AM")   # IM -> AM
print(g)
convert_graph_representation(g, "AL")   # AM -> AL
print(g)

print("\n\n---------------------------------------- AD. 1.2 ----------------------------------------")

# drawing a graph
convert_graph_representation(g, "AM")
g.draw(600, 600)

print("\n\n---------------------------------------- AD. 1.3 ----------------------------------------")

# random graph - Erdos-Renyi model based on number of edges
g.make_random_graph_edge_number(17, 21)
print(g)
g.draw()
# random graph - probability model
g.make_random_graph_probability(100, 0.03)
print(g)
g.draw()

# print("\n\n---------------------------------------- BONUS ----------------------------------------")
#
# number_of_graphs_to_generate = input("How many random graphs do you want to generate and draw? ")
# # draw some random graphs
# for _ in range(int(number_of_graphs_to_generate)):
#     g.make_random_graph_probability(randrange(5, 50), random())
#     print(g)
#     g.draw(600, 600)
