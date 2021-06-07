from src.objects.WeightedDigraph import WeightedDigraph
from src.objects.Digraph import Digraph
from src.objects.DigraphManager import DigraphManager
from src.objects.WeightedDigraphManager import WeightedDigraphManager

from src.algorithms.strong_connectivity import kosaraju, construct_strongly_connected_digraph
from src.algorithms.shortest_weighted_digraph_paths import bellman_ford, distance_matrix_from_bellman_ford, johnson

print("\n\n---------------------------------------- AD. 4.1 ----------------------------------------")
# DIGRAPH FROM FILE
dg1 = Digraph(file_path="example_data/proj4_digraph1.txt")
dg1.draw()
dg1 = Digraph(file_path="example_data/proj4_digraph2.txt")
dg1.draw()
print(dg1, '\n')
for elem in dg1.data:
    print(elem)

# RANDOM DIGRAPH FROM G(n,p) MODEL
dg2 = DigraphManager.make_random_digraph_probability(10, 0.3)
dg2.draw()
dg2 = DigraphManager.make_random_digraph_probability(10, 0.3)
dg2.draw()

print("\n\n---------------------------------------- AD. 4.2 ----------------------------------------")
# DIGRAPH DFS
res = kosaraju(dg1)
print(res)
dg1.draw()

print("\n\n---------------------------------------- AD. 4.3 ----------------------------------------")
dg3 = construct_strongly_connected_digraph(10, p=0.0)
print(dg3)
dg3.draw()

wdg1 = WeightedDigraphManager.make_weighted_digraph_from_digraph(dg3)
wdg1.draw()

BF_result = bellman_ford(wdg1)
print("Bellman-Ford algorithm result:\n", BF_result)

distance_matrix_from_bellman_ford(wdg1)

# DISTANCE MATRIX OF DIGRAPH BY BELLMAN_FORD ALGORITHM FOR RANDOM DIGRAPH
wdg2 = WeightedDigraphManager.construct_strongly_connected_weighted_digraph_probability(5, 0.3, -5, 10)
wdg2.draw()
distance_matrix_from_bellman_ford(wdg2)
johnson(wdg2)

# DISTANCE MATRIX OF DIGRAPH BY BELLMAN_FORD ALGORITHM FOR EXAMPLE DIGRAPH
wdg3 = WeightedDigraph(file_path="example_data/proj4_wdigraph1.txt")
print(wdg3)
distance_matrix_from_bellman_ford(wdg3)

print("\n\n---------------------------------------- AD. 4.4 ----------------------------------------")
# DISTANCE MATRIX OF DIGRAPH BY JOHNSON ALGORITHM FOR EXAMPLE DIGRAPH
wdg4 = WeightedDigraph(file_path="example_data/proj4_wdigraph1.txt")
johnson(wdg4)
wdg4.draw()
