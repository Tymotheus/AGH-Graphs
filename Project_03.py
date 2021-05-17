from src.objects.WeightedGraphManager import WeightedGraphManager
from src.objects.WeightedGraph import WeightedGraph

from src.algorithms.shortest_weighted_paths import *
from src.algorithms.minimum_spanning_trees import kruskal

print("\n\n---------------------------------------- AD. 3.1 ----------------------------------------")

# READ WEIGHTED GRAPH FROM FILE
g = WeightedGraph("example_data/proj3b_am.txt")
g.draw()

# CONNECTED WEIGHTED GRAPH USING PRUFER CODE AND ERDOS-RENYI MODEL
g1 = WeightedGraphManager.construct_weighted_graph_edge_number(15, 20)
g1.draw()

# CONNECTED WEIGHTED GRAPH USING PRUFER CODE AND GILBERT MODEL
g3 = WeightedGraphManager.construct_weighted_graph_probability(15, 0.5)
g3.draw()

print("\n\n---------------------------------------- AD. 3.2 ----------------------------------------")

# DIJKSTRA ALGORITHM
distanceAndPaths = dijkstra(g, 1, True)

print("\n\n---------------------------------------- AD. 3.3 ----------------------------------------")

# VERTEX DISTANCE MATRIX
vertexDistanceMatrix = create_vertex_distance_matrix(g, True)

# ADDITIONAL - DRAWING PATH
print(distanceAndPaths)
for i in range(len(distanceAndPaths)-1):
    target_vertex = i+1
    g.draw(vertices=distanceAndPaths[target_vertex], 
        edges=[[distanceAndPaths[target_vertex][i], 
        distanceAndPaths[target_vertex][i+1]] for i in range(len(distanceAndPaths[target_vertex])-1)])

print("\n\n---------------------------------------- AD. 3.4 ----------------------------------------")

# CENTER OF GRAPH
center = center_of_weighted_graph(g, vertexDistanceMatrix)
print("Center = " + str(center[1:]) + " (sum of distances: " + str(center[0]) + ")")

# MINIMAX CENTER OF GRAPH
minimaxCenter = minimax_center_of_weighted_graph(g, vertexDistanceMatrix)
print("Minimax center = " + str(minimaxCenter["minimax_center"]) + " (distance to farthest: " + str(minimaxCenter["dist_to_farthest"]) + ")")

print("\n\n---------------------------------------- AD. 3.5 ----------------------------------------")

# MINIMUM SPANNING TREE
wg5 = WeightedGraph("example_data/proj3b_am.txt")
kruskal_result = kruskal(wg5)
wg5.draw(vertices=[i for i in range(len(wg5.data))], edges=kruskal_result["mst_edges"])
mst = kruskal_result["mst"]
mst.draw()
print("MST has the sum of weight equal to: " + str(kruskal_result["weight_sum"]))
