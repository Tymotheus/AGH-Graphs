import os

from src.objects.Sequence import Sequence
from src.objects.Graph import Graph
from src.algorithms.degree_sequences import isDegreeSequence, \
    get_degree_sequence_from_graph, \
    construct_graph_from_degree_sequence

os.system('cls')

seq = Sequence()
g = Graph()

print("\n\n---------------------------------------- AD. 2.1 ----------------------------------------")

# CHECKING WHETHER A SEQUENCE IS A DEGREE SEQUENCE OF A GRAPH
for file_path in ["example_data/proj2_seq_no.txt", "example_data/proj2_seq_yes.txt"]:
    seq.read_sequence_from_file(file_path)
    ans = "Sequence " + str(seq) + " is " \
          + ("" if isDegreeSequence(seq, show_steps=True) else "not ") \
          + "a degree sequence of a graph.\n"
    print(ans)

# GETTING A DEGREE SEQUENCE OF A GRAPH
g.read_graph_from_file("example_data/proj1_al.txt", 'AL')
print(g)
seq = get_degree_sequence_from_graph(g)
print(seq)
ans = "Sequence " + str(seq) + " is " \
      + ("" if isDegreeSequence(seq, show_steps=False) else "not ") \
      + "a degree sequence of a graph.\n"
print(ans)

# CONSTRUCT A GRAPH FROM A DEGREE SEQUENCE
g1 = construct_graph_from_degree_sequence(seq)
print(g1)
g1.draw(600, 600)

print("\n\n---------------------------------------- AD. 2.2 ----------------------------------------")



print("\n\n---------------------------------------- AD. 2.5 ----------------------------------------")

# GENERATE A RANDOM K-REGULAR GRAPH
# TO DO: add randomization ?
while 1:
    try:
        print("Press k to finish")
        n = input("n = ") 
        if n == 'k':
            break
        n = int(n)
        k = int(input("k = "))

        seq = Sequence()
        seq.generate_regular_sequence(n, k)
        if isDegreeSequence(seq):
            print("Sequence " + str(seq) + " is a degree sequence of a graph.")
            g = construct_graph_from_degree_sequence(seq)
            print(g)
            g.draw(600, 600)
        else:
            print("Cannot create graph sequence for n=" + str(n) + " and k=" + str(k) + ".")

    except ValueError:
        print("n and k should be an integer")