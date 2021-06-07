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
            self.data = [[None]]
            self.representation = "AM"
        else:
            with open(file_path, 'r') as f:
                data = [[int(val) if '.' not in val else None for val in line.split(' ')] if line != '\n' else [] for line in f]
            if conversion_check_map[representation](data, digraph=True) is True:
                self.data = data
                self.representation = representation
                if show_info is True:
                    print("Weighted digraph has been read from file.")
                    print("Weighted digraph represented by adjacency matrix.")
            else:
                self.data = None
                self.representation = None
                print("Cannot read weighted digraph from file - passed data is not of the form of passed representation.")

    def draw(self, weights = [], vertices=None, arcs=None, img_width=600, img_height=600):
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

        w = weights if len(weights) else self.data
        if len(weights):
            print("tak")

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
                if self.data[i][j] is not None:
                    draw_weighted_digraph_arc(canvas, n, v_r,
                                              positions[i][0], positions[i][1], positions[j][0], positions[j][1],
                                              str(w[i][j]), "black", "gray")

        if len(arcs):
            for arc in arcs:
                if self.data[arc[0]][arc[1]] is not None:
                    i = arc[0]
                    j = arc[1]
                    draw_weighted_digraph_arc(canvas, n, v_r,
                                              positions[i][0], positions[i][1], positions[j][0], positions[j][1],
                                              str(self.data[i][j]), "red", "red")
        elif len(vertices):
            for v1 in range(len(vertices)):
                for v2 in range(len(vertices)):
                    if self.data[vertices[v1]][vertices[v2]] is not None and v1 != v2:
                        i = vertices[v1]
                        j = vertices[v2]
                        draw_weighted_digraph_arc(canvas, n, v_r,
                                                  positions[i][0], positions[i][1], positions[j][0], positions[j][1],
                                                  str(self.data[i][j]), "red", "red")

        print("Weighted digraph is being drawn.")
        canvas.pack()
        root.mainloop()

    def __str__(self):
        """String representation of a weighted digraph depending on the .representation field."""

        if self.data is None:
            graph_as_string = "Weighted digraph is empty (no data)."
        elif self.representation == 'AM':
            graph_as_string = "Adjacency matrix of weighted digraph WD:\n" + '\n'.join([''.join(['{:5}'.format(item if item is not None else '    .') for item in row]) for row in self.data])
        else:
            graph_as_string = "Cannot describe weighted digraph - unknown representation."
        return graph_as_string


def draw_weighted_digraph_arc(canvas, n, v_r, v1_x, v1_y, v2_x, v2_y, arc_value_text, arc_color, arc_value_color):
    """
    Auxiliary function to draw an arc during WeightedDigraph drawing.
    :param canvas: tkinter canvas on which the WeightedDigraph will be drawn
    :param n: order of WeightedDigraph
    :param v_r: radius of vertex
    :param v1_x: X position of vertex number 1
    :param v1_y: Y position of vertex number 1
    :param v2_x: X position of vertex number 2
    :param v2_y: Y position of vertex number 2
    :param arc_value_text: arc's flow and capacity that will be drawn on the arc
    :param arc_color: color of the arc
    :param arc_value_color: color of the arc's flow and capacity
    :return: None
    """
    a = None
    equal_x = math.fabs(v2_x - v1_x) <= 10 ** -3
    equal_y = math.fabs(v2_y - v1_y) <= 10 ** -3
    if not equal_x:
        a = -(v2_y - v1_y) / (v2_x - v1_x)
    x = 0 if equal_x else v_r if equal_y else math.sqrt(v_r ** 2 / (a ** 2 + 1))
    y = 0 if equal_y else v_r if equal_x else math.fabs(a * x)
    x_sign = 1 if v1_x < v2_x else -1
    y_sign = 1 if v1_y < v2_y else -1

    canvas.create_line(v1_x + x_sign * x, v1_y + y_sign * y,
                       v2_x - x_sign * x, v2_y - y_sign * y,
                       fill=arc_color, arrow=tk.LAST)
    canvas.create_text((2 * v1_x + v2_x) / 3,
                       (2 * v1_y + v2_y) / 3,
                       text=arc_value_text,
                       font=("Verdana", max(int(20 - 2 * n / 10), 10)),
                       fill=arc_value_color)
