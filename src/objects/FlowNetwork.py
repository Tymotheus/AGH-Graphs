import tkinter as tk
import math

from src.algorithms.representation_checks import *


class FlowNetwork:
    """Representation of a flow network. It is composed of both basic information and functionalities connected with flow networks.
    .data - stores information about its vertices and weighted arcs (both current flow and capacity)
        The element data[i][j][0] correspond to the current flow of i-j arc, and data[i][j][1] stores the information about i-j arc capacity.
    .representation - kind of flow network interpretation. The following are available:
        AM - Adjacency Matrix"""

    def __init__(self, file_path=None, representation='AM', layers=None, show_info=True):
        """ FlowNetwork constructor.
                When file_path argument is passed it reads a graph data from file.
                    The file data should be similar to a digraph data with flow network restrictions:
                        1. The first vertex is always interpreted as a source vertex s and the last vertex is interpreted as sink vertex t.
                        2. There are no two-way arcs, that is, if there exist an arc i-j, there is not arc j-i
                        3. There is no v-s arc for any vertex v.
                        4. There is no t-v arc for any vertex v.
                        5. Weights of arcs are interpreted as their maximum capacity (the initial flow will be equal to 0).
                Otherwise it creates a flow network composed only of source s and sink t vertices linked by an s-t arc of capacity 1.
            file_path - path to file with graph data. If not passed graph will be an isolated vertex represented by adjacency matrix
            representation - representation of a graph
            layers - an array contains the number of vertices that should be placed in one layer.
                This argument matters mostly in case of constructing new flow network and drawing flow network.
                The array should meet the following requirements:
                    1. Vertices s and t should be excluded because they are placed in their individual layers by default.
                    2. In one layer there cannot be more vertices than the number of all layers minus 2 (source and sink layers excluded).
                    3. The sum of values from the array increased by 2 (source and sink vertices) should match the number of vertices (i.e. in file if file_path was passed)
                By default equal to None which means that vertices (except s and t) will be divided evenly among their layers.
            show_info - boolean whether to print information about the graph after its creation."""

        if file_path is None:
            self.data = [[[0, 0], [0, 1]], [[0, 0], [0, 0]]]
            self.representation = "AM"
            self.layers = layers
        else:
            with open(file_path, 'r') as f:
                data = [[[0, int(num)] for num in line.split(' ')] if line != '\n' else [] for line in f]
            if conversion_check_map[representation](data, flow_network=True) is True:
                self.data = data
                self.representation = representation
                self.layers = layers
                if layers is not None:
                    num_of_layers = len(layers)
                    if sum(layers) + 2 != len(self.data):
                        print("The number of vertices in passed layers' array does not match the number of inner vertices (that is, s and t excluded) in flow network.")
                        return
                    for num in layers:
                        if num > num_of_layers:
                            self.data = None
                            self.representation = None
                            self.layers = None
                            print("Cannot read flow network - there cannot be more vertices in one layer than the number of inner layers.")
                if show_info is True:
                    print("Flow network has been read from file.")
                    print("Flow network represented by adjacency matrix.")
            else:
                self.data = None
                self.representation = None
                self.layers = None
                print("Cannot read flow network from file - passed data is not of the form of passed representation.")

    def draw(self, img_width=600, img_height=600):
        """ Draws the flow network in new window which pops up. The flow network should be represented by adjacency matrix.
            On each arc there is placed it's current flow F and maximum capacity C in the "F/C" format.
                img_width - width of the popped window (in pixels)
                img_height - height of the popped window (in pixels)"""

        if self.data is None:
            print("Flow network is empty (no data) - cannot draw the flow network.")
            return
        if self.representation != "AM":
            print("Flow network is not represented by adjacency matrix - convert the flow network before drawing.")
            return

        n = len(self.data)

        v_r = img_width / (3 * n) * (1 if n > 2 else 0.5)

        root = tk.Tk()
        root.geometry(str(img_height) + "x" + str(img_width))
        canvas = tk.Canvas(root, height=img_height, width=img_width, bg="white")

        positions = [[0.0] * 2 for _ in range(n)]

        draw_layers = []
        draw_layers.append([0])
        if self.layers is not None:
            for elem in self.layers:
                draw_layers.append(elem)
        else:
            num_inner_verts = n-2
            num_inner_layers = math.ceil(math.sqrt(num_inner_verts))
            verts_to_add = [i for i in range(1, n-1)]
            for i in range(num_inner_layers, 0, -1):
                layer_to_add = []
                num_of_verts_to_add = math.ceil(len(verts_to_add) / float(i))
                for j in range(num_of_verts_to_add):
                    layer_to_add.append(verts_to_add[0])
                    verts_to_add.remove(verts_to_add[0])
                draw_layers.append(layer_to_add)
        draw_layers.append([n-1])
        num_layers = len(draw_layers)

        h_break = img_width / num_layers

        for i in range(len(draw_layers)):
            x_pos = h_break/2 + h_break * i
            v_break = img_height / (len(draw_layers[i])+1)
            for j in range(len(draw_layers[i])):
                positions[draw_layers[i][j]][0], positions[draw_layers[i][j]][1] = x_pos, (v_break + j * v_break)

        texts = [str(i) for i in range(n)]
        texts[0], texts[n-1] = 's', 't'
        for i in range(n):
            canvas.create_oval(positions[i][0] - v_r, positions[i][1] - v_r,
                               positions[i][0] + v_r, positions[i][1] + v_r,
                               fill="black")
            canvas.create_text(positions[i][0], positions[i][1],
                               fill="white", text=texts[i], font=("Verdana", max(int(20 - 2 * n / 10), 10)))

        for i in range(n):
            for j in range(n):
                if self.data[i][j][1] > 0:
                    draw_flow_network_arc(canvas, v_r,
                                          positions[i][0], positions[i][1], positions[j][0], positions[j][1],
                                          f'{self.data[i][j][0]}/{self.data[i][j][1]}', "black", "gray")

        print("Flow network is being drawn.")
        canvas.pack()
        root.mainloop()

    def __str__(self):
        """String representation of a flow network depending on the .representation field."""

        if self.data is None:
            graph_as_string = "Flow network is empty (no data)."
        elif self.representation == 'AM':
            graph_as_string = "Adjacency matrix of flow network FN:\n" + '\n'.join([''.join(['{:10}'.format(f'{item[0]} / {item[1]}') for item in row]) for row in self.data])
        else:
            graph_as_string = "Cannot describe flow network - unknown representation."
        return graph_as_string


def draw_flow_network_arc(canvas, v_r, v1_x, v1_y, v2_x, v2_y, arc_value_text, arc_color, arc_value_color):
    a = None
    equal_x = math.fabs(v2_x - v1_x) <= 10 ** -3
    equal_y = math.fabs(v2_y - v1_y) <= 10 ** -3
    if not equal_x:
        a = -(v2_y - v1_y) / (v2_x - v1_x)

    x_sign = 1 if v1_x < v2_x else -1
    y_sign = 1 if v1_y < v2_y else -1

    x = 0 if equal_x else v_r if equal_y else math.sqrt(v_r ** 2 / (a ** 2 + 1))
    y = 0 if equal_y else v_r if equal_x else math.fabs(a * x)
    canvas.create_line(v1_x + x_sign * x, v1_y + y_sign * y,
                       v2_x - x_sign * x, v2_y - y_sign * y,
                       fill=arc_color, arrow=tk.LAST)

    x = 0 if equal_x else 2.5 * v_r if equal_y else math.sqrt((2.5 * v_r) ** 2 / (a ** 2 + 1))
    y = 0 if equal_y else 2.5 * v_r if equal_x else math.fabs(a * x)
    canvas.create_text(v1_x + x_sign * x, v1_y + y_sign * y,
                       text=arc_value_text,
                       font=("Verdana", 12), fill=arc_value_color)