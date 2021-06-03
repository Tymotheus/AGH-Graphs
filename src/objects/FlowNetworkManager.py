from copy import deepcopy

from random import randint, sample, random

from src.objects.FlowNetwork import FlowNetwork
from src.objects.WeightedDigraph import WeightedDigraph


class FlowNetworkManager:
    """Representation of a flow network manager which allows to execute some operations connected with flow networks."""

    def __init__(self):
        """FlowNetworkManager constructor. Simply prints that an instance of the FlowNetworkManager have been created."""

        print("FlowNetworkManager has been created")


    @staticmethod
    def construct_flow_network_edge_number(number_of_inner_layers=0, bonus_arcs=0, c_min=1, c_max=10):
        """Creates and returns flow network with given number of inner layers and probability of arc existence equal to p.
        Arcs' capacities are defined by passed arguments.
            number_of_inner_layers - number of inner layers in flow network, that is, except source and sink layers
                By default equal to 0.
            bonus_arcs - maximum number of bonus arcs which will be added to flow network after it's creation
                By default equal to 0.
                If bonus_arcs exceeds the number of arcs which are possible to add, then all possible arcs are added to the flow network.
            c_min - minimum arc capacity in flow network, by default equal to 1
            c_max - maximum arc capacity in flow network, by default equal to 10"""

        if number_of_inner_layers < 0:
            print("Number of inner layers in flow network cannot be negative.")
            return
        if bonus_arcs < 0:
            print("Number of bonus arcs in flow network cannot be negative.")
            return
        if c_min < 0 or c_max < 0 or c_min > c_max:
            print("Capacities in flow network must be greater than zero and c_min must be less of equal to c_max.")
            return

        fn = FlowNetwork()
        fn.layers = []
        n = 2

        for i in range(number_of_inner_layers):
            num_of_vertices_to_add = randint(2, number_of_inner_layers)
            n += num_of_vertices_to_add
            fn.layers.append(num_of_vertices_to_add)

        max_num_of_arcs = n * (n - 1) / 2

        fn.data = [[[0, 0] for _ in range(n)] for _ in range(n)]

        layers_with_vertices = [[0]]
        v = 1
        for layer in fn.layers:
            layer_to_add = []
            for i in range(layer):
                layer_to_add.append(v)
                v += 1
            layers_with_vertices.append(layer_to_add)
        layers_with_vertices.append([v])

        for i in range(len(layers_with_vertices)-1):
            first_layer = layers_with_vertices[i]
            second_layer = layers_with_vertices[i+1]
            from_first = False
            to_second = False
            first_layer_cpy = deepcopy(first_layer)
            second_layer_cpy = deepcopy(second_layer)
            while from_first is False or to_second is False:
                v_from_first = first_layer_cpy[randint(0, len(first_layer_cpy)-1)]
                v_from_second = second_layer_cpy[randint(0, len(second_layer_cpy) - 1)]
                fn.data[v_from_first][v_from_second][1] = randint(c_min, c_max)
                max_num_of_arcs -= 1
                first_layer_cpy.remove(v_from_first)
                second_layer_cpy.remove(v_from_second)
                if len(first_layer_cpy) == 0:
                    from_first = True
                    first_layer_cpy = deepcopy(first_layer)
                if len(second_layer_cpy) == 0:
                    to_second = True
                    second_layer_cpy = deepcopy(second_layer)

        if bonus_arcs:
            bonus_arcs_indexes = []
            if bonus_arcs >= max_num_of_arcs:
                bonus_arcs = int(max_num_of_arcs)
                bonus_arcs_indexes = [i for i in range(bonus_arcs)]
            else:
                bonus_arcs_indexes = sample(range(0, int(max_num_of_arcs)), bonus_arcs)
            index = 0
            for i in range(n):
                for j in range(n):
                    if i != j and j != 0 and i != n-1:
                        if fn.data[i][j][1] == 0 and fn.data[j][i][1] == 0:
                            if index in bonus_arcs_indexes:
                                if random() > 0.5:
                                    fn.data[i][j][1] = randint(c_min, c_max)
                                else:
                                    if i != 0 and j != n-1:
                                        fn.data[j][i][1] = randint(c_min, c_max)
                                    else:
                                        fn.data[i][j][1] = randint(c_min, c_max)
                            index += 1

        return fn

    @staticmethod
    def get_residual_network_of_flow_network(fn):
        if not isinstance(fn, FlowNetwork):
            print("Passed argument is not a flow network.")
            return

        n = len(fn.data)

        wd = WeightedDigraph()
        wd.data = [[None] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if fn.data[i][j][1]:
                    wd.data[i][j] = fn.data[i][j][1] - fn.data[i][j][0]
                    wd.data[j][i] = fn.data[i][j][0]

        return wd
