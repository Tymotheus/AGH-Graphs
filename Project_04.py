from src.objects.Digraph import Digraph
from src.objects.DigraphManager import DigraphManager
from src.objects.WeightedDigraphManager import WeightedDigraphManager

from src.algorithms.strong_connectivity import kosaraju, construct_strongly_connected_digraph

print("\n\n---------------------------------------- AD. 4.1 ----------------------------------------")

# DIGRAPH FROM FILE
# dg1 = Digraph(file_path="example_data/proj4_digraph1.txt")
dg1 = Digraph(file_path="example_data/proj4_digraph2.txt")
# dg1.draw()

# RANDOM DIGRAPH FROM G(n,p) MODEL
# dg2 = DigraphManager.make_random_digraph_probability(10, 0.3)
# dg2.draw()


print("\n\n---------------------------------------- AD. 4.2 ----------------------------------------")

# DIGRAPH TRANSPOSE
# dg1_t = DigraphManager.construct_transpose_digraph_from_digraph(dg1)
# dg1.draw()
# dg1_t.draw()

# DIGRAPH DFS
res = kosaraju(dg1)
print(res)
dg1.draw()

print("\n\n---------------------------------------- AD. 4.3 ----------------------------------------")
# dg3 = construct_strongly_connected_digraph(10, p=0.0)
# print(dg3)
# dg3.draw()

# wdg1 = WeightedDigraphManager.make_weighted_digraph_from_digraph(dg3)
# wdg1.draw()

# wdg2 = WeightedDigraphManager.construct_strongly_connected_weighted_digraph_probability(10, 0.3, -5, 10)
# wdg2.draw(vertices=[0, 1, 2, 5])
# print(wdg2)

print("\n\n---------------------------------------- AD. 4.4 ----------------------------------------")
