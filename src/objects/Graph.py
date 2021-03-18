from random import random, sample
import scipy.special
import tkinter as tk
import math

from src.algorithms.representation_conversions import convert_graph_representation


class Graph:
    def __init__(self):
        self.data = []
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

    def make_random_graph_edge_number(self, n, m):
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
        print("Random graph has been created (Erdos-Renyi model: n = " + str(n) + ", m = " + str(m) + ").")
        print("Graph represented by adjacency matrix.")

    def make_random_graph_probability(self, n, p):
        self.mode = 'AM'
        self.data = [[0] * n for _ in range(n)]
        for i in range(1, n):
            for j in range(0, i):
                if random() <= p:
                    self.data[i][j] = self.data[j][i] = 1
        print("Random graph has been created (probability model: n = " + str(n) + ", p = " + "{:.2f}".format(p) + ").")
        print("Graph represented by adjacency matrix.")

    def draw(self, img_width, img_height):
        starting_representation = self.mode
        if starting_representation != "AM":
            convert_graph_representation(self, "AM")
        n = len(self.data)
        angle = 2 * math.pi / n

        g_center_width = img_width / 2
        g_center_height = img_height / 2
        g_r = g_center_width * 2 / 3
        v_r = g_r / n

        root = tk.Tk()
        root.geometry(str(img_height)+"x"+str(img_width))
        canvas = tk.Canvas(root, height=img_height, width=img_width, bg="white")

        positions = [[0.0]*2 for _ in range(n)]

        for i in range(n):
            v_angle = i * angle
            positions[i][0] = g_center_height + g_r * math.sin(v_angle)
            positions[i][1] = g_center_width - g_r * math.cos(v_angle)

            canvas.create_oval(positions[i][0]-v_r, positions[i][1]-v_r,
                               positions[i][0]+v_r, positions[i][1]+v_r,
                               fill="black")
            canvas.create_text(positions[i][0] + (1 + n/10) * v_r * math.sin(v_angle),
                               positions[i][1] - (1 + n/10) * v_r * math.cos(v_angle),
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

    def __str__(self):
        if self.mode == 'AM':
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
