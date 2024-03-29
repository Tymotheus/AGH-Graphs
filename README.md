# AGH - Graphs and Their Uses
Tasks for "Graphs and Their Uses" course at AGH UST.

The project was developed and tested in Python 3.8 in Windows system.

Each project is shortly described in the list below. 
Details about each class, method and functionality such as arguments or certain requirements are described in the appropriate file as docstrings.


# PROJECT 1
To run solutions of tasks from project it's enough to run the Project_01.py file.
The solutions use: 
1. Graph.py - represent simple graphs.
    * reading graph data from file and printing it;
    * drawing a graph.
2. GraphManager.py - allow to perform some operations connected with simple graphs.
    * constructing random graphs using Erdos-Renyi model and Gilbert model.
3. representation_checks.py - check correctness of graph representation.
    * checking whether passed graph data, that is adjacency matrix, incidence matrix or adjacency list, is correct.
4. representation_conversions.py - convert graph representation from one to the other.
    * checking graph representation and converting it to the other.


# PROJECT 2
To run solutions of tasks from project it's enough to run the Project_02.py file.
The solutions use: 
1. Some functionalities from previous project described above.
2. GraphManager.py - allow to perform some operations connected with simple graphs.
    * randomizing edges in graph.
3. Sequence.py and Stack.py - custom implementation of sequences and stacks.
    * reading data from files and lists;
    * performing characteristic operations such as adding or removing elements.
4. degree_sequences.py - allow to perform operations connected with degree sequence of a graph.
    * checking whether sequence is a degree sequence using Havel-Hakimi algorithm;
    * constructing a degree sequence from graph and vice versa.
5. dfs.py - allow to perform DFS
    * recursive DFS algorithm implementation
5. regularity.py - allow to perform operations connected with regular graphs.
    * checking whether a graph is regular;
    * constructing a regular graph using degree sequence.
6. connectivity.py - allow to perform operations connected with connected graphs.
    * checking whether a graph is connected;
    * extracting components of a graph (maximum component in particular).
7. eulerianity.py - allow to perform operation connected with eulerian graphs.
    * checking whether a graph is eulerian;
    * constructing an eulerian graph;
    * extracting eulerian cycle from graph.
8. hamiltonicity.py - allow to perform operation connected with hamiltonian graphs.
    * extracting hamiltonian cycle from graph;
    * optimized extracting of hamiltonian cycle from graph using S. Martello approach.


# PROJECT 3
To run solutions of tasks from project it's enough to run the Project_03.py file.
The solutions use: 
1. Some functionalities from previous projects described above.
2. WeightedGraph.py - represent weighted graphs.
    * reading weighted graph data from file and printing it;
    * drawing a weighted graph.
3. WeightedGraphManager.py - allow to perform some operations connected with weighted graphs.
    * constructing weighted graph from simple graph;
    * constructing random connected weighted graphs using Prufer code, Erdos-Renyi model and Gilbert model.
4. connectivity.py - allow to perform operations connected with connected graphs.
    * constructing random connected trees using Prufer code
    * constructing random connected graphs using Prufer code followed with Erdos-Renyi model and Gilbert model.
5. shortest_weighted_paths.py - allow to find objects connected with shortest distance in weighted graphs.
    * implementation of Dijkstra algorithm;
    * finding distance matrix between any two vertices;
    * finding center and minimax-center.
6. minimum_spanning_trees.py - allow to find minimum spanning tree of weighted graph.
    * implementation of Kruskal algorithm.


# PROJECT 4
To run solutions of tasks from project it's enough to run the Project_04.py file.
The solutions use: 
1. Some functionalities from previous projects described above.
2. Digraph.py - represent digraphs.
    * reading digraphs data from file and printing it;
    * drawing a digraphs.
3. DigraphManager.py - allow to perform some operations connected with digraphs.
    * constructing random digraph using Gilbert model;
    * constructing transpose digraph of passed digraph.
4. WeightedDigraph.py - represent weighted digraphs.
    * reading weighted digraphs data from file and printing it;
    * drawing a digraphs.
5. WeightedDigraphManager.py - allow to perform some operations connected with weighted digraphs.
    * constructing weighted digraph from passed digraph;
    * constructing random weighted digraph using Gilbert model.
6. strong_connectivity.py - allow to perform some operations connected with strongly connected digraphs.
    * implementation of Kosaraju algorithm;
    * constructing strongly connected digraph using modified implementation of Tarjan algorithm.
7. shortest_weighted_digraph_paths.py - allow to find objects connected with shortest distance in weighted digraphs.
    * implementation of Bellman-Ford algorithm;
    * finding distance matrix between any two vertices using Bellman-Ford algorithm;
    * implementation of Johnson algorithm.

# PROJECT 5
To run solutions of tasks from project it's enough to run the Project_05.py file.
The solutions use: 
1. Some functionalities from previous projects described above.
2. FlowNetwork.py - represent flow networks.
    * reading weighted graph data from file and printing it;
    * drawing a weighted graph.
3. FlowNetworkManager.py - allow to perform some operations connected with flow networks.
    * constructing random flow network using layers approach and Erdos-Renyi model;
    * constructing residual network of passed flow network.
4. maximum_flow.py - allow to find maximum flow of flow network.
    * implementation of Ford-Fulkerson algorithm;
    * finding augmenting path (as a part of Ford-Fulkerson algorithm) in flow flow network using BFS.
5. representation_checks.py - check correctness of flow network representation.
    * checking whether passed flow network data is correct (improved is_adjacency_matrix function)

# PROJECT 6
To run solutions of tasks from project it's enough to run the Project_06.py file.
Example solutions of TSP problem (using implemented algorithm) are placed in tsp_results directory.
The solutions use: 
1. Some functionalities from previous projects described above.
2. WeightedGraphManager.py - allow to perform some operations connected with weighted graphs.
    * added constructing weighted graph from metric data;
3. traveling_salesman_problem.py - allow to find TSP solution.
    * getting length of cycle in weighted graph
    * perform 2-opt algorithm on weighted graph
    * perform simulated annealing algorithm on weighted graph
    * implementation of Metropolis–Hastings algorithm using 2-opt and simulated annealing to find TSP solution
    * saving found TSP solution as a diagram to a .png file