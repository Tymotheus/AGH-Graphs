from random import shuffle, random, sample
from math import fabs, exp, inf
from time import time
import matplotlib.pyplot as plt

from src.objects.WeightedGraph import WeightedGraph


def get_length_of_cycle_in_weighted_graph(wg: WeightedGraph, vertices_cycle: list):
    """
    Function to find and return the length of cycle in weighted graph.
    :param wg: WeightedGraph object
    :param vertices_cycle: list of consecutive vertices on cycle
        First and last vertices on the list should be the same.
    :return: length of vertices_cycle cycle in weighted graph wg
    """

    length = inf

    if isinstance(vertices_cycle, list):
        if vertices_cycle[0] != vertices_cycle[-1]:
            print("Passed data is not a cycle.")
        else:
            if isinstance(wg, WeightedGraph):
                length = 0
                cycle_len = len(vertices_cycle)
                for i in range(cycle_len-2):
                    first_vertex = vertices_cycle[i]
                    second_vertex = vertices_cycle[i+1]
                    length += wg.data[first_vertex][second_vertex]
            else:
                print("Passed data is not a WeightedGraph object.")
    else:
        print("No valid cycle was passed.")
    return length


def perform_2_opt_on_list(P: list, n: int = None):
    """
    Implementation of 2-opt algorithm.
    :param P: list of consecutive vertices on path
    :param n: number of vertices in graph
    :return: new list of consecutive vertices after performing 2-opt algorithm on passed list P
    """

    a_index = c_index = 0
    while fabs(a_index - c_index) <= 1 or fabs(a_index - c_index) == n:
        a_index, c_index = sample(range(0, n), 2)
    if a_index > c_index:
        a_index, c_index = c_index, a_index
    P_new = [P[a_index], P[c_index]]
    for j in range(c_index - 1, a_index, -1):
        P_new.append(P[j])
    for j in range(c_index + 1, n):
        P_new.append(P[j])
    for j in range(a_index + 1):
        P_new.append(P[j])
    return P_new


def tsp_simulated_annealing(wg: WeightedGraph, starting_cycle: list = None, MAX_IT: int = 100):
    """
    Implementation of simulated annealing algorithm.
    :param wg: WeightedGraph object
    :param starting_cycle: starting list of consecutive vertices on cycle
    :param MAX_IT: number of iterations in simulated annealing
    :return: dictionary object of simulated annealing solution data containing:
        1. found minimum hamiltonian cycle
        2. length of found minimum hamiltonian cycle
    """

    if not isinstance(wg, WeightedGraph):
        print("Passed graph is not a WeightedGraph object.")
        return {"tsp_hamiltonian_cycle": None, "tsp_cycle_length": inf}
    n = len(wg.data)

    if isinstance(starting_cycle, list):
        P = starting_cycle
    elif starting_cycle is None:
        P = [i for i in range(n)]
        shuffle(P)
        P.append(P[0])
    else:
        print("Passed cycle is not a valid object.")
        return {"tsp_hamiltonian_cycle": None, "tsp_cycle_length": inf}

    for i in range(100, 0, -1):
        T = 0.001 * (i**2)
        for it in range(MAX_IT):
            P_new = perform_2_opt_on_list(P, n)
            d_P = get_length_of_cycle_in_weighted_graph(wg, P)
            d_P_new = get_length_of_cycle_in_weighted_graph(wg, P_new)
            if d_P_new < d_P:
                P = P_new
            else:
                if random() < exp(- (d_P_new - d_P)/T):
                    P = P_new

    return {"tsp_hamiltonian_cycle": P, "tsp_cycle_length": get_length_of_cycle_in_weighted_graph(wg, P)}


def traveling_salesman_problem(wg: WeightedGraph,
                               simulated_annealing_MAX_IT: int = 100,
                               num_of_calls: int = 100,
                               show_info: bool = False):
    """
    Implementation of Metropolis–Hastings algorithm using 2-opt and simulated annealing to find TSP solution.
    :param wg: WeightedGraph object
    :param simulated_annealing_MAX_IT: number of iterations in simulated annealing
    :param num_of_calls: number of calls of simulated annealing
    :param show_info: boolean whether to print information about TSP solution
    :return: dictionary object of TSP solution data containing:
        1. found minimum hamiltonian cycle
        2. length of found minimum hamiltonian cycle
        3. number of iterations in simulated annealing
        4. number of calls of simulated annealing
        5. execution time of the algorithm
    """

    minimum_hamiltonian_cycle_data = {'cycle': None,
                                      'length': inf,
                                      'sa_iter': simulated_annealing_MAX_IT,
                                      'tsp_iter': num_of_calls,
                                      'execution_time': 0.0}
    execution_time = 0

    for i in range(num_of_calls):
        start_time = time()
        sa_result = tsp_simulated_annealing(wg=wg,
                                            starting_cycle=minimum_hamiltonian_cycle_data['cycle'],
                                            MAX_IT=simulated_annealing_MAX_IT)
        execution_time += time() - start_time

        if sa_result['tsp_cycle_length'] < minimum_hamiltonian_cycle_data['length']:
            minimum_hamiltonian_cycle_data['cycle'] = sa_result['tsp_hamiltonian_cycle']
            minimum_hamiltonian_cycle_data['length'] = sa_result['tsp_cycle_length']

        if show_info:
            print("CALLS DONE: " + str(i + 1) + " / " + str(num_of_calls))

    minimum_hamiltonian_cycle_data['execution_time'] = execution_time

    if show_info:
        print('minimum hamiltonian cycle:\n', minimum_hamiltonian_cycle_data['cycle'])
        print('minimum hamiltonian cycle length:\n', '{:.2f}'.format(minimum_hamiltonian_cycle_data['length']))
        print('time execution of ' + str(num_of_calls) + ' calls: ', '{:.3f}'.format(execution_time))
        print('average time of execution: ', '{:.3f}'.format(execution_time / num_of_calls))

    return minimum_hamiltonian_cycle_data


def save_tsp_solution_diagram(file_path: str, minimum_hamiltonian_cycle_data: dict = None):
    """
    Function saving TSP solution to .png file as a diagram.
        File will be saved in tsp_results directory. Name of file consist of TSP solution data.
    :param file_path: path to file with input data
    :param minimum_hamiltonian_cycle_data: dictionary data with TSP solution data returned by traveling_salesman_problem function
    :return: None
    """

    if file_path is None:
        print("No file was passed.")
    elif minimum_hamiltonian_cycle_data is None:
        print("No hamiltonian cycle data was passed.")
    else:
        with open(file_path, 'r') as f:
            data = [[float(val) for val in line.split()] if line != '\n' else [] for line in f]
        for i in range(len(minimum_hamiltonian_cycle_data['cycle'])-1):
            v1 = minimum_hamiltonian_cycle_data['cycle'][i]
            v2 = minimum_hamiltonian_cycle_data['cycle'][i+1]
            plt.plot([data[v1][0], data[v2][0]], [data[v1][1], data[v2][1]], 'ro-')
        plt.xlabel('x')
        plt.ylabel('y')

        output_name = 'tsp_results/tsp'
        output_name += '_' + str(len(minimum_hamiltonian_cycle_data['cycle'])-1) + 'v'
        output_name += '_' + str(int(minimum_hamiltonian_cycle_data['length'])) + 'len'
        output_name += '_' + str(minimum_hamiltonian_cycle_data['sa_iter']) + 'sa'
        output_name += '_' + str(minimum_hamiltonian_cycle_data['tsp_iter']) + 'tsp'
        output_name += '_' + str(minimum_hamiltonian_cycle_data['tsp_iter']) + 'tsp'
        output_name += '_' + str(int(minimum_hamiltonian_cycle_data['execution_time'])) + 's'
        output_name += '.png'

        plt.savefig(output_name)
        # plt.show()
        plt.close()
