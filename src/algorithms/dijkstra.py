
def dijkstra(weightedGraph, origin, show = False):
    """"Function returns matrix in which:
    matrix[0] is a list of distance from origin vertex to every other vertex
    matrix[1-...] are the paths from origin to every vertex.
    Vertex are counting from 1. 
    If input origin is greater than number of vertex then it is reduced to maximum vertex.
    If input show is True then distance and paths are printed."""
    n = len(weightedGraph.data)
    if origin < 1:
        origin = 1
        print("Origin has been upgraded to 1")
    if origin > n:
        origin = n
        print("Origin has been reduced to " + str(origin))
    origin -= 1
    distance = {i: float('inf') for i in range(n)}
    copyDistance = {i: float('inf') for i in range(n)}
    distance[origin] = 0
    copyDistance[origin] = 0
    
    predecessor = [None for _ in range(n)]
    S = []
    while len(S) < n:
        (u, d) = min(copyDistance.items(), key=lambda x: x[1]) 
        S.append(u)
        copyDistance.pop(u)
        
        for v in range(len(distance)):
            if weightedGraph.data[v][u] and distance[v] > (distance[u] + weightedGraph.data[v][u]):
                distance[v] = distance[u] + weightedGraph.data[v][u]
                copyDistance[v] = distance[u] + weightedGraph.data[v][u]
                predecessor[v] = u+1  
    matrix = [[] for _ in range(len(distance)+1)]
    matrix[0] = [i for i in distance.values()]
    for v in range(len(distance)):
        path = []
        element = predecessor[v]
        path.append(v+1)
        while element:
            path.append(element)
            element = predecessor[element-1]
        path.reverse()
        matrix[v+1] = path
    matrix[origin+1] = [origin+1]
    if show:
        print("Strat s = " + str(origin+1))
        for v in range(n):
            print("d("+ str(v+1) +") = " + str(matrix[0][v]) + " ==> " + str(matrix[v+1]))
    for i in range(1, n):
        for j in range(len(matrix[i])):
            matrix[i][j] -= 1
    return matrix

def create_vertex_distance_matrix(weightedGraph, show = False):
    """Function returns vertex distance matrix, if input show is True then the matrix is printed."""
    n = len(weightedGraph.data)
    distanceMatrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        matrix = dijkstra(weightedGraph, i+1)
        distanceMatrix[i] = matrix[0]
    if show:
        for i in range(n):
            print(distanceMatrix[i])
    
    return distanceMatrix

def center_of_weighted_graph(weightedGraph, distanceMatrix=[]):
    """Function returns number of vertex which is the center of a WeightedGraph and sum of its distances to every other vertex."""
    n = len(weightedGraph.data)
    if not len(distanceMatrix):
        distanceMatrix = create_vertex_distance_matrix(weightedGraph)
    sums = {i:sum(distanceMatrix[i]) for i in range(n)}
    (index, s) = min(sums.items(), key=lambda x: x[1]) 
    return {"center":index+1, "sum_of_distance":s}

def minimax_center_of_weighted_graph(weightedGraph, distanceMatrix=[]):
    """Function returns minimax center which has the less distance to the farthest vertex, 
    sum of distances to every other vertex and value of its distance to the farthest vertex"""
    n = len(weightedGraph.data)
    if not len(distanceMatrix):
        distanceMatrix = create_vertex_distance_matrix(weightedGraph)
    maximums = {i:max(distanceMatrix[i]) for i in range(n)}
    (index, minimum) = min(maximums.items(), key=lambda x: x[1]) 
    return {"minimax_center":index+1, "sum_of_distance":sum(distanceMatrix[index]), "dist_to_farthest":minimum}