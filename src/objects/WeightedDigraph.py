import tkinter as tk
import math

from src.algorithms.representation_checks import *


class WeightedDigraph:
    """Representation of a weighted digraph. It is composed of both basic information and functionalities connected with weighted digraphs.
    .data - stores information about its vertices and weighted arcs
    .representation - kind of graph interpretation. The following are available:
        AM - Adjacency Matrix"""

    def __init__(self, file_path=None, representation='AM', show_info=True):
        """ WeightedDigraph constructor. When file_path argument is passed it reads a graph data from file. Otherwise it creates a weighted digraph composed of isolated vertex represented by adjacency matrix.
            file_path - path to file with graph data. If not passed graph will be an isolated vertex represented by adjacency matrix
            representation - representation of a graph
            show_info - boolean whether to print information about the graph after its creation."""

        if file_path is None:
            self.data = [[0]]
            self.representation = "AM"
        else:
            with open(file_path, 'r') as f:
                data = [[int(num) for num in line.split(' ')] if line != '\n' else [] for line in f]
            if conversion_check_map[representation](data, digraph=True) is True:
                self.data = data
                self.representation = representation
                if show_info is True:
                    print("Weighted digraph has been read from file.")
                    print("Weighted digraph represented by adjacency matrix.")
            else:
                print("Cannot read weighted digraph from file - passed data is not of the form of passed representation.")

    def draw(self, vertices=None, arcs=None, img_width=600, img_height=600, flagy=None):
        """ Draws the weighted digraph in new window which pops up. The weighted digraph should be represented by adjacency matrix.
            Weights of arcs are placed closer to first vertex of each arc.
                vertices - set of vertices to distinguish which is helpful during components consideration
                arcs - set of arcs to distinguish; if None, all arcs between vertices from vertices set will be distinguished
                img_width - width of the popped window (in pixels)
                img_height - height of the popped window (in pixels)"""

        if self.data is None:
            print("Weighted digraph is empty (no data) - cannot draw the graph.")
            return
        if self.representation != "AM":
            print("Weighted digraph is not represented by adjacency matrix - convert the digraph before drawing.")
            return
        if vertices is None:
            vertices = []
        if arcs is None:
            arcs = []
        n = len(self.data)
        angle = 2 * math.pi / n

        g_center_width = img_width / 2
        g_center_height = img_height / 2
        g_r = g_center_width * 2 / 3
        v_r = g_r / n * (1 if n > 2 else 0.5)

        root = tk.Tk()
        root.geometry(str(img_height) + "x" + str(img_width))
        canvas = tk.Canvas(root, height=img_height, width=img_width, bg="white")

        positions = [[0.0] * 2 for _ in range(n)]

        for i in range(n):
            v_angle = i * angle
            positions[i][0] = g_center_height + (g_r * math.sin(v_angle) if n > 1 else 0)
            positions[i][1] = g_center_width - (g_r * math.cos(v_angle) if n > 1 else 0)

            fill_color = "red" if len(vertices) and i in vertices else "black"

            canvas.create_oval(positions[i][0] - v_r, positions[i][1] - v_r,
                               positions[i][0] + v_r, positions[i][1] + v_r,
                               fill=fill_color)
            canvas.create_text(positions[i][0] + (1 + n / 7) * v_r * math.sin(v_angle),
                               positions[i][1] - (1 + n / 7) * v_r * math.cos(v_angle),
                               text=i + 1, font=("Verdana", max(int(20 - 2 * n / 10), 10)))
        for i in range(n):
            for j in range(n):
                if self.data[i][j]:
                    a = None
                    if positions[j][0] > positions[i][0]:
                        a = -(positions[j][1] - positions[i][1]) / (positions[j][0] - positions[i][0])
                    elif positions[j][0] < positions[i][0]:
                        a = -(positions[i][1] - positions[j][1]) / (positions[i][0] - positions[j][0])
                    x = 0 if positions[j][0] == positions[i][0] else v_r if positions[j][1] == positions[i][
                        1] else math.sqrt(v_r ** 2 / (a ** 2 + 1))
                    y = 0 if positions[j][1] == positions[i][1] else v_r if positions[j][0] == positions[i][
                        0] else math.fabs(a * x)
                    # print("%.5s\t%.5s\t%.5s\t\t%.5s\t%.5s\t%.5s\t\t%.5s\t%.5s\t%.5s" %(i+1, positions[i][0], positions[i][1], j+1, positions[j][0], positions[j][1], a, x, y))
                    flagx = 1 if positions[i][0] < positions[j][0] else -1
                    flagy = 1 if positions[i][1] < positions[j][1] else -1

                    canvas.create_line(positions[i][0] + flagx * x, positions[i][1] + flagy * y,
                                       positions[j][0] - flagx * x, positions[j][1] - flagy * y,
                                       fill="black", arrow=tk.LAST)
                    canvas.create_text((2 * positions[i][0] + positions[j][0]) / 3,
                                       (2 * positions[i][1] + positions[j][1]) / 3,
                                       text=str(self.data[i][j]),
                                       font=("Verdana", max(int(20 - 2 * n / 10), 10)),
                                       fill="gray")

        if len(arcs):
            for arc in arcs:
                if self.data[arc[0]][arc[1]]:
                    i = arc[0]
                    j = arc[1]
                    a = None
                    if positions[j][0] > positions[i][0]:
                        a = -(positions[j][1] - positions[i][1]) / (positions[j][0] - positions[i][0])
                    elif positions[j][0] < positions[i][0]:
                        a = -(positions[i][1] - positions[j][1]) / (positions[i][0] - positions[j][0])
                    x = 0 if positions[j][0] == positions[i][0] else v_r if positions[j][1] == positions[i][
                        1] else math.sqrt(v_r ** 2 / (a ** 2 + 1))
                    y = 0 if positions[j][1] == positions[i][1] else v_r if positions[j][0] == positions[i][
                        0] else math.fabs(a * x)
                    # print("%.5s\t%.5s\t%.5s\t\t%.5s\t%.5s\t%.5s\t\t%.5s\t%.5s\t%.5s" % (
                    #     i + 1, positions[i][0], positions[i][1], j + 1, positions[j][0], positions[j][1], a, x, y))
                    flagx = 1 if positions[i][0] < positions[j][0] else -1
                    flagy = 1 if positions[i][1] < positions[j][1] else -1

                    canvas.create_line(positions[i][0] + flagx * x, positions[i][1] + flagy * y,
                                       positions[j][0] - flagx * x, positions[j][1] - flagy * y,
                                       fill="red", arrow=tk.LAST)
                    canvas.create_text((2 * positions[i][0] + positions[j][0]) / 3,
                                       (2 * positions[i][1] + positions[j][1]) / 3,
                                       text=str(self.data[i][j]),
                                       font=("Verdana", max(int(20 - 2 * n / 10), 10)),
                                       fill="red")
        elif len(vertices):
            for v1 in range(len(vertices)):
                for v2 in range(len(vertices)):
                    if self.data[vertices[v1]][vertices[v2]] and v1 != v2:
                        i = vertices[v1]
                        j = vertices[v2]
                        a = None
                        if positions[j][0] > positions[i][0]:
                            a = -(positions[j][1] - positions[i][1]) / (positions[j][0] - positions[i][0])
                        elif positions[j][0] < positions[i][0]:
                            a = -(positions[i][1] - positions[j][1]) / (positions[i][0] - positions[j][0])
                        x = 0 if positions[j][0] == positions[i][0] else v_r if positions[j][1] == positions[i][
                            1] else math.sqrt(v_r ** 2 / (a ** 2 + 1))
                        y = 0 if positions[j][1] == positions[i][1] else v_r if positions[j][0] == positions[i][
                            0] else math.fabs(a * x)
                        # print("%.5s\t%.5s\t%.5s\t\t%.5s\t%.5s\t%.5s\t\t%.5s\t%.5s\t%.5s" % (
                        #     i + 1, positions[i][0], positions[i][1], j + 1, positions[j][0], positions[j][1], a, x, y))
                        flagx = 1 if positions[i][0] < positions[j][0] else -1
                        flagy = 1 if positions[i][1] < positions[j][1] else -1

                        canvas.create_line(positions[i][0] + flagx * x, positions[i][1] + flagy * y,
                                           positions[j][0] - flagx * x, positions[j][1] - flagy * y,
                                           fill="red", arrow=tk.LAST)
                        canvas.create_text((2 * positions[i][0] + positions[j][0]) / 3,
                                           (2 * positions[i][1] + positions[j][1]) / 3,
                                           text=str(self.data[i][j]),
                                           font=("Verdana", max(int(20 - 2 * n / 10), 10)),
                                           fill="red")

        print("Weighted digraph is being drawn.")
        canvas.pack()
        root.mainloop()

    def __str__(self):
        """String representation of a weighted digraph depending on the .representation field."""

        if self.data is None:
            graph_as_string = "Weighted digraph is empty (no data)."
        elif self.representation == 'AM':
            graph_as_string = "Adjacency matrix of weighted digraph WD:\n"
            print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in self.data]))
        else:
            graph_as_string = "Cannot describe weighted digraph - unknown representation."
        return graph_as_string
