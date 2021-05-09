# AGH - Graphs and Their Uses
Tasks for "Graphs and Their Uses" course at AGH UST.
The project requires Python in version 3.8 or higher.

# PROJECT 1
To run solutions of tasks from project it's enough to run the Project_01.py file.
The solutions use: 
1. Graph.py file to represent graphs using some sort of graph manager (reading graph from file, drawing graph, making random graph etc.).
2. representation_checks.py to check correctness of graph representation.
3. representation_conversions.py to convert graph representation from one to the other.

# PROJECT 2


# PROJECT 3
1. To create weighted graph you can use one of two methods from WeightedGraphManager:
    >construct_weighted_graph_edge_number(n, m, w_min=1, w_max=10)
    >construct_weighted_graph_probability(n, p, w_min=1, w_max=10)
    
    Both methods return WeightedGraph which can be drawn by mehod draw()
    You can also read WeightedGraph from file:
    >read_from_file(path)

2. To print the shortes paths from one vertex to every other you can use WeightedGraph method:
    >dijkstra(graph, origin)
    where graph is a WeightedGraph and origin is a start vertex. Input origin should be an integer in range from 1 to max graph's vertex, if it is greater then method reduce it to maximum value.


# PROJECT 4


# PROJECT 5


# PROJECT 6

