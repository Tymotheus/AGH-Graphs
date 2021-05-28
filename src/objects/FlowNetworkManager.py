import copy

from random import randint

from src.objects.FlowNetwork import FlowNetwork


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

        # creating random flow network

        return fn
