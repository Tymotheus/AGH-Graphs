import tkinter as tk
import math

from src.algorithms.representation_checks import *


class WeightedGraph:
    """Representation of an undirected weighted graph, without labels.

    Stores information about its vertices and edges in .data field.
    It can be then interpreted using the .representation with certain values:
    AM - Adjacency Matrix
    It also consists of a few useful functions.

    By default the weighted graph is just an isolated vertex represented by adjacency matrix."""

    def __init__(self, file_path=None, representation='AM', show_info=True):
        """Weighted graph constructor.
            file_path - path to file with graph data. If not passed graph will be an isolated vertex represented by adjacency matrix
            representation - representation of a graph
            show_info - boolean whether to print information about the graph after its creation."""

        if file_path is None:
            self.data = [0]
            self.representation = representation
        else:
            with open(file_path, 'r') as f:
                data = [[int(num) for num in line.split(' ')] if line != '\n' else [] for line in f]
            if conversion_check_map[representation](data) is True:
                self.data = data
                self.representation = representation
                if show_info is True:
                    print("Graph has been read from file.")
                    print("Graph represented by " +
                          ("adjacency matrix." if self.representation == "AM"
                           else ("incidence matrix." if self.representation == "IM"
                                 else "adjacency list.")))
            else:
                print("Cannot read graph from file - passed data is not of the form of passed graph representation.")

    def draw(self, vertices=None, img_width=600, img_height=600):
        """ Pops up a new window with the given graph drawn in it.
            vertices - set of vertices to distinguish which is helpful during components consideration
            img_width - width of the popped window (in pixels)
            img_height - height of the popped window (in pixels)"""

        if self.data is None:
            print("Graph is empty (no data) - cannot draw the graph.")
            return
        if self.representation != "AM":
            print("Graph is not represented by adjacency matrix - convert the graph before drawing.")
            return
        if vertices is None:
            vertices = []
        n = len(self.data)
        angle = 2 * math.pi / n

        g_center_width = img_width / 2
        g_center_height = img_height / 2
        g_r = g_center_width * 2 / 3
        v_r = g_r / n * (1.5 if n > 2 else 1)

        root = tk.Tk()
        root.geometry(str(img_height) + "x" + str(img_width))
        canvas = tk.Canvas(root, height=img_height, width=img_width, bg="white")

        positions = [[0.0] * 2 for _ in range(n)]

        for i in range(n):
            v_angle = i * angle
            positions[i][0] = g_center_height + (g_r * math.sin(v_angle) if n > 1 else 0)
            positions[i][1] = g_center_width - (g_r * math.cos(v_angle) if n > 1 else 0)

        for i in range(1, n):
            for j in range(0, i):
                if self.data[i][j]:
                    fill_color = "red" if len(vertices) and i in vertices and j in vertices else "gray"
                    canvas.create_line(positions[i][0], positions[i][1],
                                       positions[j][0], positions[j][1],
                                       fill=fill_color)
                    canvas.create_text((2*positions[i][0] + positions[j][0])/3,
                                       (2*positions[i][1] + positions[j][1])/3,
                                       text=str(self.data[i][j]),
                                       font=("Verdana", max(int(20 - 2*n/10), 10)),
                                       fill=fill_color)
        for i in range(n):
            fill_color = "red" if len(vertices) and i in vertices else "gray"

            canvas.create_oval(positions[i][0] - v_r, positions[i][1] - v_r,
                               positions[i][0] + v_r, positions[i][1] + v_r,
                               fill=fill_color)
            canvas.create_text(positions[i][0],
                               positions[i][1],
                               text=i+1, font=("Verdana", max(int(20 - 2 * n / 10), 10)))
            
        print("Weighted graph is being drawn.")
        canvas.pack()
        root.mainloop()

    def __str__(self):
        """String representation of a graph depending on the .representation field."""

        if self.data is None:
            graph_as_string = "Graph is empty (no data)."
        elif self.representation == 'AM':
            graph_as_string = "Adjacency matrix of graph G:\n"
            for row in self.data:
                for element in row:
                    graph_as_string = graph_as_string + str(element) + " "
                graph_as_string = graph_as_string + "\n"
        elif self.representation == "IM":
            graph_as_string = "Incidence matrix of graph G:\n"
            for row in self.data:
                for element in row:
                    graph_as_string = graph_as_string + str(element) + " "
                graph_as_string = graph_as_string + "\n"
        else:
            graph_as_string = "Cannot describe graph - unknown representation."
        return graph_as_string