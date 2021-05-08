def is_adjacency_matrix(matrix):
    '''Checks if the passed matrix is a valid Adjacency Matrix '''

    n = len(matrix)
    for i in range(n):
        if len(matrix[i]) != n:
            return False

    if matrix[0][0] != 0:
        return False
    for i in range(1, n):
        for j in range(0, i):
            # usunąć albo sprawdzać dodać do funkcji argument Graf Ważony czy coś 
            # if matrix[i][j] != 0:
            #     if matrix[i][j] != 1:
            #         return False
            if matrix[i][j] != matrix[j][i]:
                return False
        if matrix[i][i] != 0:
            return False
    return True


def is_incidence_matrix(matrix):
    '''Checks if the passed matrix is a valid Incidence Matrix '''

    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        if len(matrix[i]) != m:
            return False
    if m > (n * (n-1) / 2):
        return False
    for j in range(m):
        vertices_in_edge = 0
        first_index = second_index = None
        for i in range(n):
            if matrix[i][j] != 0:
                if matrix[i][j] != 1:
                    return False
            if matrix[i][j] == 1:
                vertices_in_edge += 1
                if first_index is None:
                    first_index = i
                else:
                    second_index = i
        if vertices_in_edge != 2:
            return False
        for j2 in range(j+1, m):
            if matrix[first_index][j] == matrix[first_index][j2] and matrix[second_index][j] == matrix[second_index][j2]:
                return False

    return True


def is_adjacency_list(adjacency_list):
    ''' Checks if the passed list/matrix is a valid Adjacency List'''

    n = len(adjacency_list)
    print(adjacency_list)
    for i in range(n):
        if len(adjacency_list[i]) > n-1:
            return False
        copies_checker = []
        for neighbour in adjacency_list[i]:
            if neighbour in copies_checker:
                return False
            if neighbour-1 == i:
                return False
            if i+1 not in adjacency_list[neighbour-1]:
                return False
            copies_checker.append(neighbour)
    return True

'''Dictionary object, to map the represantations to their proper validation functions'''
conversion_check_map = {"AM": is_adjacency_matrix,
                       "IM": is_incidence_matrix,
                       "AL": is_adjacency_list }
