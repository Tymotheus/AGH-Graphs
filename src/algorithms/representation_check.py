def is_adjacency_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        if len(matrix[i]) != n:
            return False

    if matrix[0][0] != 0:
        return False
    for i in range(1, n):
        for j in range(0, i):
            if matrix[i][j] != 0:
                if matrix[i][j] != 1:
                    return False
            if matrix[i][j] != matrix[j][i]:
                return False
        if matrix[i][i] != 0:
            return False
    return True


def is_incidence_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        if len(matrix[i]) != m:
            return False
    if m > (n * (n-1) / 2):
        return False
    for j in range(m):
        vertices_in_edge = 0
        for i in range(n):
            if matrix[i][j] == 1:
                vertices_in_edge += 1
        if vertices_in_edge != 2:
            return False
    return True


def is_adjacency_list(adjacency_list):
    n = len(adjacency_list)
    for i in range(n):
        if len(adjacency_list[i]) > n-1:
            return False
        for neighbour in adjacency_list[i]:
            if neighbour-1 == i:
                return False
            if i+1 not in adjacency_list[neighbour-1]:
                return False
    return True


conversion_check_map = {"AM": is_adjacency_matrix,
                       "IM": is_incidence_matrix,
                       "AL": is_adjacency_list}
