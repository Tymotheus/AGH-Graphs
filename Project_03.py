from src.objects.WeightedGraphManager import WeightedGraphManager

print("\n\n---------------------------------------- AD. 3.1 ----------------------------------------")

# CONNECTED WEIGHTED GRAPH USING PRUFER CODE AND ERDOS-RENYI MODEL
# g = WeightedGraphManager.construct_weighted_graph_edge_number(5, 6)
# g.draw()

# CONNECTED WEIGHTED GRAPH USING PRUFER CODE AND GILBERT MODEL
# g = WeightedGraphManager.construct_weighted_graph_probability(5, 0.5)
# g.draw()

# CONNECTED WEIGHTED GRAPH READ FROM FILE
g = WeightedGraphManager.read_from_file("example_data/proj3_am.txt")
# g.draw()

print("\n\n---------------------------------------- AD. 3.2 ----------------------------------------")

# DIJKSTRA
distance = WeightedGraphManager.dijkstra(g, 11)
g.draw()

print("\n\n---------------------------------------- AD. 3.3 ----------------------------------------")


print("\n\n---------------------------------------- AD. 3.4 ----------------------------------------")


print("\n\n---------------------------------------- AD. 3.5 ----------------------------------------")
