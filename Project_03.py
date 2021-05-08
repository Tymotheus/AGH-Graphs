import os
import time
from random import randint, uniform
os.system('cls')

from src.objects.WeightGraph import WeightGraph


print("\n\n---------------------------------------- AD. 3.1 ----------------------------------------")
# creating random WeightGraph - default max amount of vertex = 7, p = 0.5
wg = WeightGraph()
# wg.draw()

# wg = WeightGraph(15, 0.1)
# wg.draw()

# reading WeightGraph from file - is possible only as Adjacency Matrix ("AM")
wg.read_graph_from_file("example_data/proj3_am.txt", "AM")
print(wg)
wg.draw()