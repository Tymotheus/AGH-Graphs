from src.objects.FlowNetwork import FlowNetwork
from src.objects.FlowNetworkManager import FlowNetworkManager

from src.algorithms.maximum_flow import ford_fulkerson

print("\n\n---------------------------------------- AD. 5.1 ----------------------------------------")

# BASIC FLOW NETWORK
fn = FlowNetwork()
print(fn)
fn.draw()

# FLOW NETWORK FROM FILE
# fn2 = FlowNetwork('example_data/proj5_flow_network_yes.txt')
# fn2 = FlowNetwork('example_data/proj5_flow_network_no.txt')
fn2 = FlowNetwork('example_data/proj5_flow_network_yes_not_equal_layers.txt', layers=[3, 3, 2])
print(fn2)
fn2.draw()
fn2 = FlowNetwork('example_data/proj5_flow_network_yes_not_equal_layers.txt', layers=[2, 2, 2, 2])
fn2.draw()

# RANDOM FLOW NETWORK
N = 2
fn3 = FlowNetworkManager.construct_flow_network_edge_number(N, 2*N)
print(fn3)
fn3.draw()

print("\n\n---------------------------------------- AD. 5.2 ----------------------------------------")

# FORD-FULKERSON
N = 3
# fn_ff = FlowNetwork()
# fn_ff = FlowNetwork('example_data/proj5_flow_network_ford_fulkerson.txt')
fn_ff = FlowNetworkManager.construct_flow_network_edge_number(N, 2*N)
fn_ff.draw()
max_flow = ford_fulkerson(fn_ff)
print(fn_ff)
print("maximum flow of FL: ", max_flow)
fn_ff.draw()

