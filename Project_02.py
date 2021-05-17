import time
from random import randint, uniform

from src.objects.Sequence import Sequence
from src.objects.Graph import Graph
from src.objects.GraphManager import GraphManager

from src.algorithms.degree_sequences import is_degree_sequence, get_degree_sequence_from_graph, construct_graph_from_degree_sequence
from src.algorithms.regularity import construct_k_regular_graph
from src.algorithms.connectivity import get_largest_component_of_graph
from src.algorithms.eulerianity import construct_eulerian_graph, get_eulerian_cycle_of_graph
from src.algorithms.hamiltonicity import get_hamiltonian_cycle_of_graph, get_hamiltonian_cycle_of_graph_optimized


print("\n\n---------------------------------------- AD. 2.1 ----------------------------------------")

# CHECKING WHETHER A SEQUENCE IS A DEGREE SEQUENCE OF A GRAPH
seq = Sequence()
for file_path in ["example_data/proj2_seq_no.txt", "example_data/proj2_seq_yes.txt"]:
    seq.read_sequence_from_file(file_path)
    ans = "Sequence " + str(seq) + " is " \
          + ("" if is_degree_sequence(seq, show_steps=True) else "not ") \
          + "a degree sequence of a graph.\n"
    print(ans)

# GETTING A DEGREE SEQUENCE OF A GRAPH
g = Graph("example_data/proj1_al.txt", 'AL')
print(g)
seq = get_degree_sequence_from_graph(g)
print(seq)
ans = "Sequence " + str(seq) + " is " \
      + ("" if is_degree_sequence(seq, show_steps=False) else "not ") \
      + "a degree sequence of a graph.\n"
print(ans)

# CONSTRUCTING A GRAPH FROM DEGREE SEQUENCE
g1 = construct_graph_from_degree_sequence(seq)
print(g1)
# g1.draw(600, 600)

print("\n\n---------------------------------------- AD. 2.2 ----------------------------------------")

# CONSTRUCTING A GRAPH EITHER FROM DEGREE SEQUENCE OR PROBABILITY MODEL
# seq.read_sequence_from_file("example_data/proj2_seq_k_regular.txt")
# seq.read_sequence_from_file("example_data/proj2_seq_yes.txt")
# seq.read_sequence_from_file("example_data/proj2_seq_complete.txt")
# g2 = construct_graph_from_degree_sequence(seq)
g2 = GraphManager.make_random_graph_probability(100, 0.9)
# g2.draw()

# RANDOMIZING EDGES OF A GRAPH (DEGREES OF VERTICES DO NOT CHANGE)
s = get_degree_sequence_from_graph(g2)
print("Degree sequence of a graph before randomizing: " + str(s))
GraphManager.randomize(g2, show_shuffling_statistics=False)
s = get_degree_sequence_from_graph(g2)
print("Degree sequence of a graph after randomizing: " + str(s))
# g2.draw()

print("\n\n---------------------------------------- AD. 2.3 ----------------------------------------")

# CONSTRUCTING A GRAPH FROM PROBABILITY MODEL
g3 = GraphManager.make_random_graph_probability(20, 0.07)

# GET MAXIMUM COMPONENT OF A GRAPH
max_component_of_g3 = get_largest_component_of_graph(g3, show_maximum_component_result=True, show_components=True,
                                                     show_vertices_flow=False)
print(max_component_of_g3)
g3.draw(max_component_of_g3)

print("\n\n---------------------------------------- AD. 2.4 ----------------------------------------")

# CONSTRUCTING EULERIAN GRAPH
g4 = construct_eulerian_graph(10)
print(g4)

# GET EULERIAN CYCLE OF A GRAPH
eulerian_cycle_of_g4 = get_eulerian_cycle_of_graph(g4, show_cycle=True)
print(eulerian_cycle_of_g4)
# g4.draw()


print("\n\n---------------------------------------- AD. 2.5 ----------------------------------------")

# CONSTRUCTING K-REGULAR GRAPH
g5 = construct_k_regular_graph(6, 3)
# print(g5)
# g5.draw()

# RANDOMIZE EDGES OF GENERATED K-REGULAR GRAPH
GraphManager.randomize(g5, show_shuffling_statistics=False)
# print(g5)
# g5.draw()

print("\n\n---------------------------------------- AD. 2.6 ----------------------------------------")

# CONSTRUCTING A GRAPH EITHER FROM DEGREE SEQUENCE, FILE OR PROBABILITY MODEL
# for _ in range(10):
g6 = GraphManager.make_random_graph_probability(100, 0.5)
# g6.read_graph_from_file("example_data/proj2_hamiltonian_no1.txt")
# seq.read_sequence_from_file("example_data/proj2_seq_complete.txt")
# g6 = construct_graph_from_degree_sequence(seq)

# GET HAMILTONIAN CYCLE OF A GRAPH
hamiltonian_cycle_of_g6 = get_hamiltonian_cycle_of_graph(g6, show_cycle=False)
# print(hamiltonian_cycle_of_g6)
# g6.draw()

# # BONUS - COMPARING NORMAL METHOD AND OPTIMIZED ONE
# time_of_normal_version = time_of_optimized_version = 0.0
# number_of_tests = 100
# number_of_better_normal_version_tests = 0
#
# tests_start_time = time.time()
# for i in range(number_of_tests):
#     g6 = GraphManager.make_random_graph_probability(randint(75, 100), uniform(0.5, 0.75), show_info=False)
#     print("TEST " + str(i+1) + " / " + str(number_of_tests))
#
#     time_before_normal_version = time.time()
#     hamiltonian_cycle_of_g6 = get_hamiltonian_cycle_of_graph(g6, show_cycle=False)
#     time_after_normal_version = time.time()
#     time_of_normal_version += time_after_normal_version - time_before_normal_version
#
#     time_before_optimized_version = time.time()
#     hamiltonian_cycle_of_g6_opt = get_hamiltonian_cycle_of_graph_optimized(g6, show_cycle=False)
#     time_after_optimized_version = time.time()
#     time_of_optimized_version += time_after_optimized_version - time_before_optimized_version
#
#     if (time_after_normal_version - time_before_normal_version) < (time_after_optimized_version - time_before_optimized_version):
#         number_of_better_normal_version_tests += 1
# tests_finish_time = time.time()
#
# average_time_of_normal_version = time_of_normal_version / number_of_tests
# average_time_of_optimized_version = time_of_optimized_version / number_of_tests
# print("Testing elapsed: ", tests_finish_time-tests_start_time)
# print("On average normal version elapsed: ", average_time_of_normal_version)
# print("On average optimized version elapsed: ", average_time_of_optimized_version)
# print("Elapsed time ratio (normal version to optimized version): " + "{:.3f}".format(average_time_of_normal_version / average_time_of_optimized_version))
# print("Normal version was faster in " + str(number_of_better_normal_version_tests) + " tests out of " + str(number_of_tests) + ".")
