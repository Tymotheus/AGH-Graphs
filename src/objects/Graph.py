from random import random, sample, uniform
import scipy.special
import tkinter as tk
import math

from src.algorithms.representation_conversions import convert_graph_representation


class Graph:
    def __init__(self):
        self.data = None
        self.mode = None

    def read_graph_from_file(self, file_path, mode='AM'):
        with open(file_path, 'r') as f:
            self.data = [[int(num) for num in line.split(' ')] for line in f]
        print("Graph has been read from file.")
        self.mode = mode
        print("Graph represented by " +
              ("adjacency matrix." if self.mode == "AM"
               else ("incidence matrix." if self.mode == "IM"
                     else "adjacency list.")))

    def make_random_graph_edge_number(self, n, m, show_info=True):
        self.mode = 'AM'
        self.data = [[0] * n for _ in range(n)]
        v_n = scipy.special.comb(n, 2)
        smp = sample(range(1, int(v_n)), m)
        index = 1
        for i in range(1, n):
            for j in range(0, i):
                if index in smp:
                    self.data[i][j] = self.data[j][i] = 1
                index = index+1
        if show_info is True:
            print("Random graph has been created (Erdos-Renyi model: n = " + str(n) + ", m = " + str(m) + ").")
            print("Graph represented by adjacency matrix.")

    def make_random_graph_probability(self, n, p, show_info=True):
        self.mode = 'AM'
        self.data = [[0] * n for _ in range(n)]
        for i in range(1, n):
            for j in range(0, i):
                if random() <= p:
                    self.data[i][j] = self.data[j][i] = 1
        if show_info is True:
            print("Random graph has been created (probability model: n = " + str(n) + ", p = " + "{:.3f}".format(p) + ").")
            print("Graph represented by adjacency matrix.")

    def draw(self, img_width=600, img_height=600):
        if self.data is None:
            print("Graph is empty (no data) - cannot draw the graph.")
            return
        starting_representation = self.mode
        if starting_representation != "AM":
            convert_graph_representation(self, "AM")
        n = len(self.data)
        angle = 2 * math.pi / n

        g_center_width = img_width / 2
        g_center_height = img_height / 2
        g_r = g_center_width * 2 / 3
        v_r = g_r / n * (1 if n > 2 else 0.5)

        root = tk.Tk()
        root.geometry(str(img_height)+"x"+str(img_width))
        canvas = tk.Canvas(root, height=img_height, width=img_width, bg="white")

        positions = [[0.0]*2 for _ in range(n)]

        for i in range(n):
            v_angle = i * angle
            positions[i][0] = g_center_height + (g_r * math.sin(v_angle) if n > 1 else 0)
            positions[i][1] = g_center_width - (g_r * math.cos(v_angle) if n > 1 else 0)

            canvas.create_oval(positions[i][0]-v_r, positions[i][1]-v_r,
                               positions[i][0]+v_r, positions[i][1]+v_r,
                               fill="black")
            canvas.create_text(positions[i][0] + (1 + n/7) * v_r * math.sin(v_angle),
                               positions[i][1] - (1 + n/7) * v_r * math.cos(v_angle),
                               text=i+1, font=("Verdana", max(int(20 - 2*n/10), 10)))
        for i in range(1, n):
            for j in range(0, i):
                if self.data[i][j] == 1:
                    canvas.create_line(positions[i][0], positions[i][1], positions[j][0], positions[j][1])

        if starting_representation != "AM":
            convert_graph_representation(self, starting_representation)

        print("Graph is being drawn.")
        canvas.pack()
        root.mainloop()

    def randomize(self, show_shuffling_statistics=False):
        if self.data is None:
            print("Graph is empty (no data) - cannot shuffle edges.")
            return
        if self.mode != "AM":
            convert_graph_representation(self, "AM")
        n = len(self.data)
        list_of_edges = []
        for i in range(1, n):
            for j in range(0, i):
                if self.data[i][j] == 1:
                    list_of_edges.append([i, j])
        m = len(list_of_edges)
        number_of_iterations_arr = []
        exceeded = 0
        number_of_shuffles = int(0.5 * m)
        for i in range(number_of_shuffles):
            flag_shuffled = False
            number_of_iterations = 0
            max_iterations = int(uniform(2, 4) * m)
            while flag_shuffled is False and number_of_iterations < max_iterations:
                first_edge_index, second_edge_index = sample(range(0, m), 2)
                first_edge = list_of_edges[first_edge_index]
                second_edge = list_of_edges[second_edge_index]
                if first_edge[0] != second_edge[0] and first_edge[0] != second_edge[1] and first_edge[1] != second_edge[0] and first_edge[1] != second_edge[1]:
                    if self.data[first_edge[0]][second_edge[1]] == 0 and first_edge[0] != second_edge[1] and self.data[second_edge[0]][first_edge[1]] == 0 and second_edge[0] != first_edge[1]:
                        self.data[first_edge[0]][second_edge[1]] = self.data[second_edge[0]][first_edge[1]] = self.data[second_edge[1]][first_edge[0]] = self.data[first_edge[1]][second_edge[0]] = 1
                        self.data[first_edge[0]][first_edge[1]] = self.data[second_edge[0]][second_edge[1]] = self.data[first_edge[1]][first_edge[0]] = self.data[second_edge[1]][second_edge[0]] = 0
                        list_of_edges.append([first_edge[0], second_edge[1]] if first_edge[0] > second_edge[1] else [second_edge[1], first_edge[0]])
                        list_of_edges.append([second_edge[0], first_edge[1]] if second_edge[0] > first_edge[1] else [first_edge[1], second_edge[0]])
                        list_of_edges.pop(first_edge_index if first_edge_index > second_edge_index else second_edge_index)
                        list_of_edges.pop(second_edge_index if first_edge_index > second_edge_index else first_edge_index)
                        flag_shuffled = True
                    elif self.data[first_edge[0]][second_edge[0]] == 0 and first_edge[0] != second_edge[0] and self.data[second_edge[1]][first_edge[1]] == 0 and second_edge[1] != first_edge[1]:
                        self.data[first_edge[0]][second_edge[0]] = self.data[second_edge[1]][first_edge[1]] = self.data[second_edge[0]][first_edge[0]] = self.data[first_edge[1]][second_edge[1]] = 1
                        self.data[first_edge[0]][first_edge[1]] = self.data[second_edge[0]][second_edge[1]] = self.data[first_edge[1]][first_edge[0]] = self.data[second_edge[1]][second_edge[0]] = 0
                        list_of_edges.append([first_edge[0], second_edge[0]] if first_edge[0] > second_edge[0] else [second_edge[0], first_edge[0]])
                        list_of_edges.append([second_edge[1], first_edge[1]] if second_edge[1] > first_edge[1] else [first_edge[1], second_edge[1]])
                        list_of_edges.pop(first_edge_index if first_edge_index > second_edge_index else second_edge_index)
                        list_of_edges.pop(second_edge_index if first_edge_index > second_edge_index else first_edge_index)
                        flag_shuffled = True
                number_of_iterations += 1
                if number_of_iterations >= 3*m:
                    exceeded += 1
            number_of_iterations_arr.append(number_of_iterations)
        print("Shuffled edges of a graph " + str(number_of_shuffles) + " times.")
        if show_shuffling_statistics:
            print("n: " + str(n) + ", m: " + str(m) + ", average: " + str(sum(number_of_iterations_arr)/len(number_of_iterations_arr)) + ", exceeded: " + str(exceeded))

    def __str__(self):
        if self.data is None:
            res = "Graph is empty (no data)."
        elif self.mode == 'AM':
            res = "Adjacency matrix of graph G:\n"
            for row in self.data:
                for elem in row:
                    res = res + str(elem) + " "
                res = res + "\n"
        elif self.mode == "IM":
            res = "Incidence matrix of graph G:\n"
            for row in self.data:
                for elem in row:
                    res = res + str(elem) + " "
                res = res + "\n"
        else:
            res = "Adjacency list of graph G:\n"
            i = 0
            for row in self.data:
                res = res + str(i+1) + " -> "
                for elem in row:
                    res = res + "[" + str(elem) + "] "
                res = res + "\n"
                i = i + 1
        return res
