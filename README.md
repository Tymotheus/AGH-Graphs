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
1. To create weighted graph g you can use one of two methods from WeightedGraphManager:
    >g = WeightedGraphManager.construct_weighted_graph_edge_number(n, m, w_min=1, w_max=10)
    
    >g = WeightedGraphManager.construct_weighted_graph_probability(n, p, w_min=1, w_max=10)
    
    Both methods return WeightedGraph which can be drawn by mehod draw().
    You can also read WeightedGraph from file (you can only read connected weight graph):
    >g = WeightedGraphManager.read_from_file(path)

2. To print the shortes paths from one vertex to every other you can use function from dijkstra module with parameter show = True:
    >distanceAndPathMatrix = dijkstra(weightedGraph, origin, show = False)
    
    Input graph is a WeightedGraph and origin is a start vertex. Input origin should be an integer in range from 1 to max graph's vertex, if it is greater then method reduce it to maximum value. This method returns a matrix with distances and paths from origin to every other vertex.

    The path from origin to vertex i can by drawn by using distanceAndPathMatrix:
    >g.draw(distanceAndPaths[i])

    But it has a bug and sometimes draws connection with origin and destination.

3. To get vertex distance matrix of weighted graph you can use method from dijkstra module:
    >matrix = create_vertex_distance_matrix(weigtedGraph, show = False)

    If you put show = True into method then the matrix will be printed.

4. To get center and minimax center of WeightedGraph you can use function from dijkstra module:
    > center = center_of_weighted_graph(weightedGraph, vertexDistanceMatrix=[])
    
    > minimaxCenter = minimax_center_of_weighted_graph(weightedG, vertexDistanceMatrix=[])

    Both functions get WeightedGraph and additionally vertex distance matrix of the graph - second parameter can reduce time of program execution.
    Functions return dictionary with number of vetrex, its sum of distance to every other vertex and the second function also returns distance to the farthest vertex.

# PROJECT 4


# PROJECT 5


# PROJECT 6

