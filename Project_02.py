import os

from src.objects.Sequence import Sequence
from src.objects.Graph import Graph
from src.algorithms.degree_sequences import isDegreeSequence, get_degree_sequence_from_graph

os.system('cls')

seq = Sequence()
g = Graph()

print("\n\n---------------------------------------- AD. 2.1 ----------------------------------------")

# CHECKING WHETHER A SEQUENCE IS A DEGREE SEQUENCE OF A GRAPH
for file_path in ["example_data/proj2_seq_yes.txt", "example_data/proj2_seq_no.txt"]:
    seq.read_sequence_from_file(file_path)
    ans = "Sequence " + str(seq) + " is " \
          + ("" if isDegreeSequence(seq, show_steps=False) else "not ") \
          + "a degree sequence of a graph.\n"
    print(ans)

# GETTING A DEGREE SEQUENCE OF A GRAPH
# g.read_graph_from_file("example_data/proj1_al.txt", 'AL')
# print(g)
# seq = get_degree_sequence_from_graph(g)
# print(seq)
# ans = "Sequence " + str(seq) + " is " \
#       + ("" if isDegreeSequence(seq, show_steps=True) else "not ") \
#       + "a degree sequence of a graph.\n"
# print(ans)

# CONSTRUCT A GRAPH FROM A DEGREE SEQUENCE


print("\n\n---------------------------------------- AD. 2.2 ----------------------------------------")
