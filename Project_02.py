import os
import time
from random import randint, uniform

from src.objects.Sequence import Sequence
from src.objects.Graph import Graph
from src.algorithms.degree_sequences import is_degree_sequence, get_degree_sequence_from_graph, construct_graph_from_degree_sequence
from src.algorithms.regularity import construct_k_regular_graph
from src.algorithms.connectivity import get_maximum_component_of_graph
from src.algorithms.eulerianity import construct_eulerian_graph, get_eulerian_cycle_of_graph
from src.algorithms.hamiltonicity import get_hamiltonian_cycle_of_graph, get_hamiltonian_cycle_of_graph_opt
os.system('cls')


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
g = Graph()
g.read_graph_from_file("example_data/proj1_al.txt", 'AL')
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
g2 = Graph()
# seq.read_sequence_from_file("example_data/proj2_seq_k_regular.txt")
# seq.read_sequence_from_file("example_data/proj2_seq_yes.txt")
# seq.read_sequence_from_file("example_data/proj2_seq_complete.txt")
# g2 = construct_graph_from_degree_sequence(seq)
g2.make_random_graph_probability(100, 0.9)
# g2.draw()

# RANDOMIZING EDGES OF A GRAPH (DEGREES OF VERTICES DO NOT CHANGE)
s = get_degree_sequence_from_graph(g2)
print("Degree sequence of a graph before randomizing: " + str(s))
g2.randomize(show_shuffling_statistics=True)
s = get_degree_sequence_from_graph(g2)
print("Degree sequence of a graph after randomizing: " + str(s))
# g2.draw()

print("\n\n---------------------------------------- AD. 2.3 ----------------------------------------")

# CONSTRUCTING A GRAPH FROM PROBABILITY MODEL
g3 = Graph()
g3.make_random_graph_probability(20, 0.07)

# GET MAXIMUM COMPONENT OF A GRAPH
max_component_of_g3 = get_maximum_component_of_graph(g3,
                                                     show_maximum_component_result=True,
                                                     show_components=True,
                                                     show_vertices_flow=False)
# print(max_component_of_g3)
# g3.draw()

print("\n\n---------------------------------------- AD. 2.4 ----------------------------------------")

# CONSTRUCTING EULERIAN GRAPH
g4 = construct_eulerian_graph(10)
# print(g4)

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
g5.randomize(True)
# print(g5)
# g5.draw()

print("\n\n---------------------------------------- AD. 2.6 ----------------------------------------")

# CONSTRUCTING A GRAPH EITHER FROM DEGREE SEQUENCE, FILE OR PROBABILITY MODEL
g6 = Graph()

# for _ in range(10):
g6.make_random_graph_probability(100, 0.5)
# g6.read_graph_from_file("example_data/proj2_hamiltonian_no1.txt")
# seq.read_sequence_from_file("example_data/proj2_seq_complete.txt")
# g6 = construct_graph_from_degree_sequence(seq)

# GET HAMILTONIAN CYCLE OF A GRAPH
time_before_normal = time.time()
hamiltonian_cycle_of_g6 = get_hamiltonian_cycle_of_graph(g6, show_cycle=False)
time_of_normal_ver = time.time() - time_before_normal
# print(hamiltonian_cycle_of_g6)
print("Normal version elapsed: ", time_of_normal_ver)
# g6.draw()

# BONUS - COMPARING NORMAL METHOD AND OPTIMIZED ONE
time_of_normal_ver = time_of_opt_ver = 0.0
number_of_tests = 200
win_number_of_normal_version = 0

tests_start_time = time.time()
for i in range(number_of_tests):
    g6.make_random_graph_probability(randint(75, 100), uniform(0.5, 0.75), show_info=False)
    print("TEST " + str(i+1) + " / " + str(number_of_tests))

    time_before_normal = time.time()
    hamiltonian_cycle_of_g6 = get_hamiltonian_cycle_of_graph(g6, show_cycle=False)
    time_after_normal = time.time()
    time_of_normal_ver += time_after_normal - time_before_normal

    time_before_opt = time.time()
    hamiltonian_cycle_of_g6_opt = get_hamiltonian_cycle_of_graph_opt(g6, show_cycle=False)
    time_after_opt = time.time()
    time_of_opt_ver += time_after_opt - time_before_opt

    if (time_after_normal - time_before_normal) < (time_after_opt - time_before_opt):
        win_number_of_normal_version += 1
tests_finish_time = time.time()

avg_time_of_normal_ver = time_of_normal_ver/number_of_tests
avg_time_of_opt_ver = time_of_opt_ver/number_of_tests
print("Testing elapsed: ", tests_finish_time-tests_start_time)
print("On average normal version elapsed: ", avg_time_of_normal_ver)
print("On average optimized version elapsed: ", avg_time_of_opt_ver)
print("Elapsed time ratio (normal version to optimized version): " + "{:.3f}".format(avg_time_of_normal_ver/avg_time_of_opt_ver))
print("Normal version was faster in " + str(win_number_of_normal_version) + " tests out of " + str(number_of_tests) + ".")
