from src.objects.WeightedGraphManager import WeightedGraphManager
from src.algorithms.dijkstra import *

print("\n\n---------------------------------------- AD. 3.1 ----------------------------------------")

# # CONNECTED WEIGHTED GRAPH USING PRUFER CODE AND ERDOS-RENYI MODEL
g = WeightedGraphManager.construct_weighted_graph_edge_number(7, 8)
g.draw()

# # CONNECTED WEIGHTED GRAPH USING PRUFER CODE AND GILBERT MODEL
g = WeightedGraphManager.construct_weighted_graph_probability(5, 0.5)
g.draw()

# CONNECTED WEIGHTED GRAPH READ FROM FILE
g = WeightedGraphManager.read_from_file("example_data/proj3b_am.txt")
g.draw()

print("\n\n---------------------------------------- AD. 3.2 ----------------------------------------")

# DIJKSTRA ALGORITHM
distanceAndPaths = dijkstra(g, 1, True)

print("\n\n---------------------------------------- AD. 3.3 ----------------------------------------")

# VERTEX DISTANCE MATRIX
vertexDistanceMatrix = create_vertex_distance_matrix(g, True)

# ADDITIONAL - DRAWING PATH - DOESN'T WORK PROPERLY - drawing edge beetwen origin and the end vertex sometimes
g.draw(distanceAndPaths[5])

print("\n\n---------------------------------------- AD. 3.4 ----------------------------------------")

# CENTER OF GRAPH
center = center_of_weighted_graph(g, vertexDistanceMatrix)
print("Center of graph: " + str(center["center"]) + " with sum = " + str(center["sum_of_distance"]))

# MINIMAX CENTER OF GRAPH
minimaxCenter = minimax_center_of_weighted_graph(g, vertexDistanceMatrix)
print("Minimax center of graph: " 
    + str(minimaxCenter["minimax_center"]) + " with sum = " 
    + str(minimaxCenter["sum_of_distance"]) + " and distance to the farthest vertex = " 
    + str(minimaxCenter["dist_to_farthest"]))

# print("\n\n---------------------------------------- AD. 3.5 ----------------------------------------")
