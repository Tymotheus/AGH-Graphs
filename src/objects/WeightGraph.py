from src.objects.Graph import Graph
from src.algorithms.connectivity import get_maximum_component_of_graph

from random import random, randrange, sample
import tkinter as tk
import math

class WeightGraph(Graph):
    
    def __init__(self, n=7, p=0.5):
        self.representation = 'AM'
        self.data = [[0] * n for _ in range(n)]
        for i in range(1, n):
            for j in range(0, i):
                if random() <= p:
                    self.data[i][j] = self.data[j][i] = randrange(0, 11) 
        component = get_maximum_component_of_graph(self)
        
        # max_num_of_edges = n * (n-1) / 2
        # indexes_of_existing_edges = sample(range(0, int(max_num_of_edges)), n-1)
        # index = 0
        # for i in range(1, n):
        #     for j in range(0, i):
        #         if index in indexes_of_existing_edges:
        #             self.data[i][j] = self.data[j][i] = randrange(0, 11) 
        #         index = index+1
        # print(self)
        # print(component)
        
        # deleting not connected vertex
        dataSize = len(component)
        if dataSize < len(self.data):
            newData = [[0] * dataSize for _ in range(dataSize)]
            i = 0
            j = 0
            for c_i in component:
                for c_j in component:
                    newData[i][j] = self.data[c_i][c_j]
                    j+=1
                j = 0
                i +=1
            self.data = newData


    def draw(self, component=[], img_width=600, img_height=600):
        if self.data is None:
            print("Graph is empty (no data) - cannot draw the graph.")
            return
        if self.representation != "AM":
            convert_graph_representation(self, "AM")
        n = len(self.data)
        angle = 2 * math.pi / n

        g_center_width = img_width / 2
        g_center_height = img_height / 2
        g_r = g_center_width * 2 / 3
        v_r = g_r / n * (1.5 if n > 2 else 1)

        root = tk.Tk()
        root.geometry(str(img_height)+"x"+str(img_width))
        canvas = tk.Canvas(root, height=img_height, width=img_width, bg="white")

        positions = [[0.0]*2 for _ in range(n)]

        for i in range(n):
            v_angle = i * angle
            positions[i][0] = g_center_height + (g_r * math.sin(v_angle) if n > 1 else 0)
            positions[i][1] = g_center_width - (g_r * math.cos(v_angle) if n > 1 else 0)

        for i in range(1, n):
            for j in range(0, i):
                if self.data[i][j]: # == 1
                    fillColor = "red" if len(component) and i in component else "gray"
                    canvas.create_line(positions[i][0], positions[i][1], positions[j][0], positions[j][1], fill=fillColor)
                    canvas.create_text((2*positions[i][0] + positions[j][0])/3 ,
                                       (2*positions[i][1] + positions[j][1])/3 ,
                               text=str(self.data[i][j]), font=("Verdana", max(int(20 - 2*n/10), 10)), fill = fillColor)

        for i in range(n):
            fillColor = "red" if len(component) and i in component else "gray"
            canvas.create_oval(positions[i][0]-v_r, positions[i][1]-v_r,
                               positions[i][0]+v_r, positions[i][1]+v_r,
                               fill=fillColor)
            canvas.create_text(positions[i][0],
                               positions[i][1],
                               text=i, font=("Verdana", max(int(20 - 2*n/10), 10))) # text = i+1

        print("Graph is being drawn.")
        canvas.pack()
        root.mainloop()
