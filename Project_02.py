import os

from src.objects.Sequence import Sequence
from src.objects.Graph import Graph
from src.algorithms.degree_sequences import is_degree_sequence, \
    get_degree_sequence_from_graph, \
    construct_graph_from_degree_sequence
from src.algorithms.regular_graphs import construct_k_regular_graph

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

# CONSTRUCT A GRAPH FROM A DEGREE SEQUENCE
g1 = construct_graph_from_degree_sequence(seq)
print(g1)
# g1.draw(600, 600)

print("\n\n---------------------------------------- AD. 2.2 ----------------------------------------")

# SHUFFLING (CHANGING) EDGES OF A GRAPH
# seq.read_sequence_from_file("example_data/proj2_seq_k_regular.txt")
# seq.read_sequence_from_file("example_data/proj2_seq_yes.txt")
seq.read_sequence_from_file("example_data/proj2_seq_complete.txt")
g2 = construct_graph_from_degree_sequence(seq)
g2.make_random_graph_probability(100, 0.99)
# g2.draw()
for _ in range(1):
    g2.shuffle_edges(10)
    s = get_degree_sequence_from_graph(g2)
# g2.draw()

print("\n\n---------------------------------------- AD. 2.3 ----------------------------------------")


print("\n\n---------------------------------------- AD. 2.4 ----------------------------------------")


print("\n\n---------------------------------------- AD. 2.5 ----------------------------------------")

# GENERATE A K-REGULAR GRAPH
k_regular_g = construct_k_regular_graph(6, 3)
print(k_regular_g)
k_regular_g.draw()

# RANDOMIZE EDGES OF GENERATED K-REGULAR GRAPH
k_regular_g.shuffle_edges(100)
print(k_regular_g)
k_regular_g.draw()

print("\n\n---------------------------------------- AD. 2.6 ----------------------------------------")
