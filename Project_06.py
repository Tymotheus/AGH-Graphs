from src.objects.WeightedGraphManager import WeightedGraphManager
from src.algorithms.traveling_salesman_problem import traveling_salesman_problem, save_tsp_solution_diagram

file_paths = ['example_data/proj6_input59.dat', 'example_data/proj6_input200.dat']

num_of_calls = 100
sa_MAX_ITs = [20, 50, 100, 500]

for file_path in file_paths:
    cwg = WeightedGraphManager.construct_complete_weighted_graph_from_grid_data(file_path)
    for sa_MAX_IT in sa_MAX_ITs:
        minimum_hamiltonian_cycle_data = traveling_salesman_problem(wg=cwg,
                                                                    simulated_annealing_MAX_IT=sa_MAX_IT,
                                                                    num_of_calls=num_of_calls,
                                                                    show_info=True)
        save_tsp_solution_diagram(file_path, minimum_hamiltonian_cycle_data)

# print('minimum hamiltonian cycle:\n', minimum_hamiltonian_cycle_data['cycle'])
# print('minimum hamiltonian cycle length:\n', '{:.2f}'.format(minimum_hamiltonian_cycle_data['length']))
