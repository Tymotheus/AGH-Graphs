from src.objects.WeightedGraphManager import WeightedGraphManager
from src.algorithms.dijkstra import *

print("\n\n---------------------------------------- AD. 3.1 ----------------------------------------")

# CONNECTED WEIGHTED GRAPH USING PRUFER CODE AND ERDOS-RENYI MODEL
g = WeightedGraphManager.construct_weighted_graph_edge_number(15, 14)
g.draw()

# CONNECTED WEIGHTED GRAPH USING PRUFER CODE AND GILBERT MODEL
g = WeightedGraphManager.construct_weighted_graph_probability(15, 0.5)
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
# g.draw(distanceAndPaths[5])

print("\n\n---------------------------------------- AD. 3.4 ----------------------------------------")

# CENTER OF GRAPH
center = center_of_weighted_graph(g, vertexDistanceMatrix)
print("Center = " + str(center[1:]) + " (sum of distances: " + str(center[0]) + ")")

# MINIMAX CENTER OF GRAPH
minimaxCenter = minimax_center_of_weighted_graph(g, vertexDistanceMatrix)
print("Minimax center = " + str(minimaxCenter["minimax_center"]) 
    + " (distance to farthest: " + str(minimaxCenter["dist_to_farthest"]) + ")")

# print("\n\n---------------------------------------- AD. 3.5 ----------------------------------------")
